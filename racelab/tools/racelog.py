"""Telemetri proxy'si ve yarış özeti.

Agent ile TORCS arasına girer, paketleri değiştirmeden iletir ve her adımı kaydeder:

    agent  --UDP-->  proxy (listen_port)  --UDP-->  TORCS scr_server (torcs_port)
    agent  <--UDP--  proxy                <--UDP--  TORCS

Böylece mevcut agent dosyalarına dokunmadan tur süresi, hasar, çarpma sayısı,
pist dışı süre ve hız bilgisi toplanır.
"""
import csv
import re
import select
import socket
import threading
import time

_PAIR = re.compile(r"\((\w+) ([^)]*)\)")

# Her adımda telemetry.csv'ye yazılan alanlar
SENSOR_FIELDS = ["curLapTime", "lastLapTime", "distRaced", "distFromStart", "speedX",
                 "speedY", "trackPos", "angle", "damage", "gear", "rpm", "racePos"]
ACTION_FIELDS = ["accel", "brake", "steer", "gear"]

HIT_MERGE_S = 1.0  # bu süre içindeki hasar artışları tek çarpma sayılır


def parse_msg(msg):
    out = {}
    for key, val in _PAIR.findall(msg):
        parts = val.split()
        try:
            nums = [float(p) for p in parts]
        except ValueError:
            continue
        out[key] = nums[0] if len(nums) == 1 else nums
    return out


class TelemetryProxy(threading.Thread):
    def __init__(self, listen_port, torcs_port, host="127.0.0.1", torcs_host="127.0.0.1"):
        super().__init__(daemon=True)
        self.agent_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.agent_sock.bind((host, listen_port))
        self.torcs_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.torcs_addr = (torcs_host, torcs_port)
        self.agent_addr = None
        self.rows = []
        self.last_action = {}
        self.events = []  # (sim_time, text)
        self.shutdown_seen = False
        self.identified = False
        self._halt = threading.Event()

    def run(self):
        socks = [self.agent_sock, self.torcs_sock]
        while not self._halt.is_set():
            ready, _, _ = select.select(socks, [], [], 0.2)
            for s in ready:
                try:
                    data, addr = s.recvfrom(2 ** 17)
                except OSError:
                    continue  # Windows: önceki gönderim ICMP unreachable aldıysa
                if s is self.agent_sock:
                    self.agent_addr = addr
                    self.torcs_sock.sendto(data, self.torcs_addr)
                    self.last_action = parse_msg(data.decode("utf-8", "replace"))
                else:
                    if self.agent_addr:
                        self.agent_sock.sendto(data, self.agent_addr)
                    self._on_server(data.decode("utf-8", "replace"))

    def _on_server(self, msg):
        if "***identified***" in msg:
            self.identified = True
            return
        if "***shutdown***" in msg:
            self.shutdown_seen = True
            return
        if "***restart***" in msg:
            self.events.append((self.rows[-1]["curLapTime"] if self.rows else 0, "restart"))
            return
        s = parse_msg(msg)
        if "curLapTime" not in s:
            return
        row = {k: s.get(k) for k in SENSOR_FIELDS}
        row["wall"] = time.time()
        for k in ACTION_FIELDS:
            row["act_" + k] = self.last_action.get(k)
        self.rows.append(row)

    def stop(self):
        self._halt.set()
        self.join(timeout=2)
        self.agent_sock.close()
        self.torcs_sock.close()

    # ------------------------------------------------------------------ özet
    def write_csv(self, path):
        if not self.rows:
            return
        keys = list(self.rows[0].keys())
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(self.rows)

    def summary(self, laps=1):
        return summarize(self.rows, laps, self.shutdown_seen)


def summarize(rows, laps=1, shutdown_seen=False):
    if not rows:
        return {"finished": False, "steps": 0, "error": "telemetri yok (agent bağlanamadı?)"}

    hits, last_hit_t, offtrack_events, offtrack_steps = 0, -1e9, 0, 0
    was_off = False
    prev_dmg = rows[0]["damage"] or 0
    sim_t = 0.0
    laps_done = 0
    lap_times = []
    prev_last = rows[0]["lastLapTime"] or 0
    for i, r in enumerate(rows):
        sim_t = i * 0.02  # scr_server 50 Hz
        dmg = r["damage"] or 0
        if dmg > prev_dmg:
            if sim_t - last_hit_t > HIT_MERGE_S:
                hits += 1
            last_hit_t = sim_t
        prev_dmg = dmg
        off = abs(r["trackPos"] or 0) > 1.0
        if off:
            offtrack_steps += 1
            if not was_off:
                offtrack_events += 1
        was_off = off
        last = r["lastLapTime"] or 0
        if last > 0 and last != prev_last:
            laps_done += 1
            lap_times.append(last)
        prev_last = last

    speeds = [r["speedX"] or 0 for r in rows]
    final = rows[-1]
    # Sadece TORCS'un bildirdiği tur süresi bitiş sayılır. ***shutdown*** tek başına
    # yeterli değil: TORCS tur süresi limitini (~445 s) aşan aracı da yarıştan alır (DNF).
    finished = laps_done >= laps
    lap_time = lap_times[laps - 1] if finished else None
    dnf_reason = None
    if not finished:
        dnf_reason = "tur limiti aşıldı / yarış kapandı" if shutdown_seen else "yarış yarıda kesildi"
    return {
        "finished": bool(finished),
        "dnf_reason": dnf_reason,
        "lap_time_s": round(lap_time, 3) if lap_time else None,
        "lap_times": [round(x, 3) for x in lap_times],
        "damage": int(final["damage"] or 0),
        "hits": hits,
        "offtrack_events": offtrack_events,
        "offtrack_time_s": round(offtrack_steps * 0.02, 2),
        "top_speed_kmh": round(max(speeds), 1),
        "avg_speed_kmh": round(sum(speeds) / len(speeds), 1),
        "distance_m": round(final["distRaced"] or 0, 1),
        "sim_time_s": round(len(rows) * 0.02, 2),
        "steps": len(rows),
        "race_pos": int(final["racePos"] or 0),
    }
