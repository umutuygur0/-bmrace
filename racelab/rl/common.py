"""RL agent'ı için ortak parçalar: SCR protokolü, gözlem, sürüş yardımcıları.

Eğitim ortamı (torcs_env.py) ve yarış agent'ı (agents/sac_agent.py) bu modülü
paylaşır; böylece eğitimde öğrenilen politika yarışta birebir aynı girdileri görür.

Agent sadece 2 şey öğrenir:  steer ∈ [-1, 1]  ve  pedal ∈ [-1, 1]
(pedal > 0 gaz, pedal < 0 fren). Vites, ABS ve patinaj kontrolü kuraldır.
"""
import math
import re

import numpy as np

# 19 mesafe sensörünün açıları (derece). Virajı erken görmek için öne yoğun.
TRACK_ANGLES = [-90, -60, -45, -30, -20, -15, -10, -6, -3, 0, 3, 6, 10, 15, 20, 30, 45, 60, 90]
INIT_MSG = "SCR(init " + " ".join(str(a) for a in TRACK_ANGLES) + ")"

OBS_DIM = 32
ACT_DIM = 2

_PAIR = re.compile(r"\((\w+) ([^)]*)\)")


def parse(msg):
    out = {}
    for key, val in _PAIR.findall(msg):
        nums = [float(x) for x in val.split()]
        out[key] = nums[0] if len(nums) == 1 else nums
    return out


def make_obs(s, prev_action):
    """Ham sensör sözlüğü → normalize edilmiş 32 boyutlu vektör."""
    track = np.asarray(s["track"], dtype=np.float32)
    obs = np.concatenate([
        [s["angle"] / math.pi,
         np.clip(s["trackPos"], -3, 3),
         s["speedX"] / 200.0,
         s["speedY"] / 50.0,
         s["speedZ"] / 50.0],
        track / 200.0,                                        # 19 (pist dışında -1 → -0.005)
        np.asarray(s["wheelSpinVel"], dtype=np.float32) / 200.0,  # 4
        [s["rpm"] / 20000.0,
         s["gear"] / 7.0],
        prev_action,                                          # 2
    ]).astype(np.float32)
    return obs


# ----------------------------------------------------------------- sürüş yardımcıları
# car1-ow1: tork 18000 rpm'e kadar artıyor, sınırlayıcı 18700 → geç vites değiştir.
GEAR_RATIOS = [3.9, 2.9, 2.3, 1.87, 1.68, 1.54, 1.46]
UPSHIFT_RPM = 18000
MAX_GEAR = 7
WHEEL_RADIUS = [0.3179, 0.3179, 0.3307, 0.3307]  # m (12" ön / 13" arka jant + lastik)


def auto_gear(gear, rpm, speed_x):
    gear = int(gear)
    if gear < 1 or speed_x < 5:
        return 1
    if gear < MAX_GEAR and rpm > UPSHIFT_RPM:
        return gear + 1
    if gear > 1:
        down_rpm = UPSHIFT_RPM * GEAR_RATIOS[gear - 1] / GEAR_RATIOS[gear - 2] - 2000
        if rpm < down_rpm:
            return gear - 1
    return gear


def abs_brake(brake, s):
    """Tekerlek kilitleniyorsa freni azalt."""
    if brake <= 0 or s["speedX"] < 10:
        return brake
    v = s["speedX"] / 3.6
    wheel_v = np.mean([w * r for w, r in zip(s["wheelSpinVel"], WHEEL_RADIUS)])
    slip = v - wheel_v
    if slip > 2.0:
        brake = brake - min(brake, (slip - 2.0) * 0.1)
    return brake


def traction_control(accel, s):
    """Arka tekerler öndekilerden çok hızlı dönüyorsa gazı kes."""
    w = s["wheelSpinVel"]
    spin = (w[2] * WHEEL_RADIUS[2] + w[3] * WHEEL_RADIUS[3]) - (w[0] * WHEEL_RADIUS[0] + w[1] * WHEEL_RADIUS[1])
    if spin > 2.0:
        accel = max(0.0, accel - min(accel, (spin - 2.0) * 0.1))
    return accel


def to_command(action, s):
    """Politika çıktısı [steer, pedal] → SCR komut sözlüğü."""
    steer = float(np.clip(action[0], -1, 1))
    pedal = float(np.clip(action[1], -1, 1))
    accel = max(pedal, 0.0)
    brake = max(-pedal, 0.0)
    accel = traction_control(accel, s)
    brake = abs_brake(brake, s)
    if s["speedX"] < 10 and pedal > 0:  # kalkışta tam gaz desteği
        accel = max(accel, 0.5)
    gear = auto_gear(s["gear"], s["rpm"], s["speedX"])
    return {"accel": accel, "brake": brake, "gear": gear, "steer": steer, "clutch": 0.0, "meta": 0}


def command_msg(cmd):
    return ("(accel %.4f)(brake %.4f)(gear %d)(steer %.4f)(clutch %.3f)(focus 0)(meta %d)"
            % (cmd["accel"], cmd["brake"], cmd["gear"], cmd["steer"], cmd["clutch"], cmd["meta"]))
