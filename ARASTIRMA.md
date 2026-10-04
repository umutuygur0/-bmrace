# IBM TORCS Yarışı — Proje Araştırması ve Agent Geliştirme Analizi

> Bu dosya yeni oluşturulmuştur; projedeki hiçbir mevcut dosya değiştirilmemiştir.
> Klonlanan referans repolar: `rlTORCS/` ve `Torcs---Reinforcement-Learning-using-Q-Learning/`
> (salt okunur referans — derlenmedi, kurulmadı, mevcut TORCS kurulumuna dokunulmadı).

---

## 0. Yarışma hedefi (kaynak: `AI-Racing-Session-1 - Updated.pdf` ve setup rehberleri)

| | |
|---|---|
| Görev | **En hızlı tur + sıfır hasar** |
| Pist | **Corkscrew** (Road Tracks), **1 tur**, duran kalkış |
| Araç | **`scr_server 1`** (port 3001), Quick Race'te **tek sürücü** |
| Ölçülen | Tur süresi, hasar, en yüksek hız (TORCS sol üst panel) → "lap log" tablosu = teslim kanıtı |
| Takvim | S1 29 Eyl (temel tur) · S2 1 Eki (ilk iyileştirme) · S3 6 Eki (viraj/fren) · S4 8 Eki (hasarsız + dokümantasyon) · **Teslim 11 Eki** · Tören 22 Eki |
| Araçlar | IBM Bob (VS Code AI), alternatif olarak Ollama + Granite 4.0 350M + Continue.dev |

- Sunum temel sürücü olarak `snakeoil3_gym.py`'ı, setup rehberi ise ana dosya olarak `torcs_jm_par.py`'ı gösteriyor.
  İkisi aynı snakeoil iskeletini kullanıyor; RaceRunner'ın beklediği dosya `torcs_jm_par.py`.
- Organizatörlerin beklediği iyileştirmeler (slayt 29) bu analizle birebir örtüşüyor: viraj öncesi frenleme yok,
  sabit hedef hız, mesafe sensörleri kullanılmıyor, gaz adımları çok küçük, yarış çizgisi yok.
- `snakeoil3_gym.py` `drive_example`: hedef hız 300, steer = `angle·15/π − trackPos·0.10`, gaz ±0.01/adım
  (çok yavaş hızlanıyor), fren hiç yok, hıza göre vites (50/80/110/140/170).
- **Sonuç:** yarışma tek araçlı bir zaman denemesi; rakip yönetimi ve RL ortamı ikincil. En yüksek getiri
  Corkscrew'e özel **sensör tabanlı fren/hız planlaması + yarış çizgisi + hasarsızlık** (Bölüm 5, Seviye 2–3).

---

## 1. Proje nedir?

IBM'in TORCS yarışması: **TORCS** (The Open Racing Car Simulator) içinde bir arabayı
**Python ile yazılmış bir sürücü (agent)** kontrol eder. Amaç, aracı pistte tutarak
olabildiğince hızlı tur atmak / yarışı kazanmak.

### 1.1 Mimari (client–server, UDP)

```
┌──────────────────────────┐        UDP (localhost)        ┌─────────────────────────┐
│ TORCS (wtorcs.exe)       │  ── sensör mesajı (S) ──────▶ │ Python client (agent)   │
│  + scr_server robotu     │                               │  torcs_jm_par.py vb.    │
│  (SCR yarışma eklentisi) │  ◀── aksiyon mesajı (R) ───── │  drive() fonksiyonu     │
└──────────────────────────┘                               └─────────────────────────┘
   fizik 500 Hz, sürücü sorgusu 50 Hz  →  1 saniye ≈ 50 adım (step)
```

- Her `scr_server` sürücüsü **bir UDP portu** dinler: `scr_server 1 → 3001`, `2 → 3002` … `10 → 3010`
  (`torcs/drivers/scr_server/scr_server.xml` içinde index 0–9, isimleri `uni 0`…).
- Yarış **tüm scr_server sürücülerine birer client bağlanana kadar başlamaz**
  (ekranın "Yanıt Vermiyor" olmasının sebebi buydu: quickrace.xml 4 scr_server içeriyor).
- El sıkışma: client `SCR(init -45 -19 … 45)` gönderir → server `***identified***` döner.
  `init` içindeki 19 açı, **track mesafe sensörlerinin yönlerini** belirler (agent seçebilir!).
- Özel mesajlar: `***shutdown***` (yarış bitti), `***restart***` (yeniden başlat).
  Client `meta=1` göndererek yarışı yeniden başlatabilir.

### 1.2 Mesaj formatı

Server → client: `(angle 0.01)(speedX 87.2)(track 7.1 8.0 …)(trackPos -0.12)…`
Client → server: `(accel 1)(brake 0)(gear 2)(steer -0.05)(clutch 0)(focus 0)(meta 0)`

### 1.3 Sensörler (agent'ın gözlemi)

| Sensör | Anlam | Not |
|---|---|---|
| `angle` | Araç yönü ile pist ekseni arasındaki açı (rad, [-π, π]) | Direksiyonun ana girdisi |
| `trackPos` | Pist eksenine uzaklık, normalize: 0 merkez, ±1 kenar | \|x\|>1 → pist dışı |
| `track[19]` | Pist kenarına mesafe (m, ≤200), init'teki açılarda | Viraj algılama / hız planlama |
| `speedX/Y/Z` | Hız (km/h) | |
| `rpm`, `gear` | Motor devri, vites | Vites mantığı |
| `wheelSpinVel[4]` | Tekerlek dönüş hızları | Patinaj kontrolü (TCS) / ABS |
| `opponents[36]` | 10°'lik dilimlerde rakip mesafesi (≤200 m) | Çoklu araç / sollama |
| `focus[5]` | Odak sensörü | Genelde kullanılmaz |
| `damage`, `fuel`, `racePos`, `distRaced`, `distFromStart`, `curLapTime`, `lastLapTime`, `z` | Yarış durumu | Ödül/izleme |

### 1.4 Aksiyonlar

| Aksiyon | Aralık |
|---|---|
| `steer` | [-1, 1] (+1 = sol, tam kilit ≈ 0.785 rad) |
| `accel` | [0, 1] |
| `brake` | [0, 1] |
| `gear` | -1, 0, 1…6 |
| `clutch` | [0, 1] |
| `meta` | 0 / 1 (1 = yarışı yeniden başlat) |

---

## 2. Projedeki dosyalar ve rolleri

| Yol | Rol |
|---|---|
| `torcs/` | Windows TORCS kurulumu (SCR patch'li), `wtorcs.exe`, `drivers/scr_server/scr_server.dll` |
| `torcs/config/raceman/quickrace.xml` | Quick Race ayarı: E-Track 4, **4 adet scr_server** |
| `gym_torcs/torcs_jm_par.py` | **Ana yarış dosyası.** RaceRunner ile uyumlu. Parametrik kural tabanlı sürücü |
| `gym_torcs/snakeoil3_gym.py` | Snakeoil client (port 3001, `drive_example`) |
| `gym_torcs/snakeoil3_jm2.py` | Aynısı, port 3002 ve farklı kazançlar (2. araç için) |
| `gym_torcs/jmcncarai.py` | IBM'in verdiği orijinal snakeoil örneği |
| `gym_torcs/gym_torcs.py` | OpenAI-Gym benzeri RL ortamı — **Linux'a özel** (`pkill`, `xte`, port 3101, vtorcs) |
| `gym_torcs/sample_agent.py`, `example_experiment.py` | Rastgele aksiyonlu gym örneği |
| `gym_torcs/vtorcs-RL-color/` | Linux için vision destekli TORCS kaynak kodu (Windows'ta kullanılmıyor) |
| `gym_torcs/practice.xml` | 8 scr_server'lı practice ayarı (Michigan oval) |
| `RaceRunner_1.0.1_x64-setup.exe` | IBM'in yarış koşturma aracı; `torcs_jm_par.py`'ı port ve parametrelerle çağırır |
| `TORCS_Python_Windows_Troubleshooting_Guide.docx` | Windows kurulum/sorun giderme rehberi |
| `TORCS Windows setup guide.docx` | Native Windows kurulumu: venv, paketler (numpy, torch, gymnasium…), Ollama/Granite, Continue.dev |
| `TORCS container setup guide.docx` | Podman konteyneri (`johnsloe/torcs-competition`), tarayıcıdan masaüstü, port 3001 |
| `TORCS customising guide.docx` | Araç boyası / pist afişi değiştirme (sadece görsel, puanı etkilemez) |
| `AI-Racing-Session-1 - Updated.pdf` | 1. oturum sunumu: görev, kurallar, takvim, lap log |

### 2.1 `torcs_jm_par.py` sözleşmesi (bozulmaması gereken kısımlar)

- `--port/-p` → **RaceRunner yarış modunda port'u buradan verir. Port asla hardcode edilmemeli.**
- `--parameters/-f '<json>'` → practice modunda RaceRunner şu anahtarları gönderir:
  `target_speed`, `steer_gain`, `centering_gain`, `brake_threshold`, `gear_thresholds` (6 eleman), `traction_control`.
- Dosyada `REQUIRED … DO NOT CHANGE OR REMOVE` ile işaretli bloklar (port parse, `get_servers_input`,
  parametre global'leri) korunmalı. Yeni bir agent bu iskeleti **kopyalayıp** sadece `drive_*` kısmını değiştirmeli.

### 2.2 Mevcut sürücü mantığı (`drive_modular`)

```
steer  = angle * STEER_GAIN/π  − trackPos * CENTERING_GAIN      (clip [-1,1])
accel  = hız < TARGET_SPEED ise +0.4, değilse −0.2;  hız<10 ise kalkış desteği
brake  = |angle| > BRAKE_THRESHOLD (0.9 rad ≈ 51°) ise 0.3, yoksa 0
TCS    = arka teker − ön teker spin farkı > 2 ise accel −0.1
gear   = GEAR_SPEEDS eşiklerine göre (rpm'e bakmıyor)
```

**Zayıf noktalar (geliştirme fırsatları):**
1. **Viraj öncesi frenleme yok.** Fren yalnızca araç zaten ~51° savrulmuşken devreye giriyor.
   `track[9]` (ön sensör) ile "öndeki boş mesafe → güvenli hız" hesaplanmıyor.
2. Hedef hız sabit (100 km/h) → düzlükte yavaş, virajda hızlı.
3. Direksiyon yalnızca pist eksenine hizalanıyor; **yarış çizgisi** (dışarıdan gir, içe yaklaş, dışarı çık) yok.
4. Vites hıza göre; rpm tabanlı vites daha verimli.
5. ABS yok, rakip (opponents) hiç kullanılmıyor → çoklu yarışta çarpışma riski.
6. `STEER_GAIN` JSON'dan `int()` ile okunuyor → ondalık değer verilemez.

---

## 3. Referans repo #1 — `rlTORCS` (YurongYou)

**Ne:** Derin RL (görsel girdili) için **değiştirilmiş TORCS 1.3.6 C++ kaynağı** + Lua/Torch7 eğitim kodu.

### 3.1 Mimari
- **UDP yerine paylaşımlı bellek (shared memory, `mkey`)** — DeepDriving (Princeton) yöntemi.
  Özel sürücü (`ficos_discrete` / `ficos_continuous`) her adımda belleğe görüntü + durum yazar,
  agent'ın aksiyonunu bekler (`written` bayrağı ile senkron).
- `torcs _rgs <config.xml>` → **GUI menüsüne girmeden** yarış başlatma (gym_torcs'taki `xte` hack'ine gerek yok).
- `glReadPixels` ile **birinci şahıs kamera görüntüsü** (640×480) okunur; gri/RGB, 84×84'e küçültülür.
- `xvfb` ile ekransız sunucuda **paralel çoklu ortam** (A3C, 12 thread).
- Semantik segmentasyon hilesi: pistin değiştirilmiş 3D modelleriyle ikinci render alıp farkı almak.

### 3.2 RL tasarımı
- **Ayrık aksiyon (9):** {gaz, boş, fren} × {sol, düz, sağ}. Sürücü aksiyonu **kademeli** uygular
  (klavyeyle süren insan gibi; ani direksiyon yok) → öğrenmeyi stabilize ediyor.
- **Sürekli aksiyon (2):** gaz/fren ∈ [-1,1], direksiyon ∈ [-1,1].
- ABS/ASR ve vites **sabit kodlu** — agent sadece gaz/fren/direksiyon öğreniyor.
- **Ödül (Torcs.lua):** `0.005 · (v·cos(angle) − 0.01·Δhasar − 2·|pos|)`
- **Ödül (ConstDamagePos):** hasar/sıkışma → `-0.025`; aksi halde `0.006 · (v·cos(angle) − 0.3·|pos|)`
- Bitiş: `isEnd`, 10000 adım, hasar > 90000, 500 adım sıkışma (|angle|>50° ve v<1).
- Sonuç: A3C, 2e7 adım, 84×84 gri görüntü, lr 7e-5 → Ushite-city'de başarılı sürüş.

### 3.3 Bizim projeye uygunluğu
- ❌ **Doğrudan kullanılamaz:** Linux + Lua Torch7 + TORCS'un yeniden derlenmesi gerekiyor.
  `install.sh` sistemdeki TORCS'un yerine geçer — **mevcut Windows ortamına kurulmamalı.**
- ❌ Yarışma SCR/UDP protokolünü ve sensör tabanlı client'ı kullanıyor; görsel girdi yarışmada yok.
- ✅ **Alınacak fikirler:**
  - Ödül şekli: `v·cos(angle) − k·|trackPos| − hasar cezası` (gym_torcs ile aynı aile, kanıtlanmış).
  - **Kademeli/yumuşatılmış aksiyon** (rate limiting) — direksiyon salınımını keser.
  - Vites/ABS/TCS'yi kuralla çöz, agent'a sadece gaz-fren-direksiyon öğret.
  - Sıkışma algılama + otomatik reset (`meta=1`).
  - Paralel ortam fikri → bizde: farklı portlarda birden çok scr_server ile paralel veri toplama.

---

## 4. Referans repo #2 — `Torcs---Reinforcement-Learning-using-Q-Learning` (A-Raafat)

**Ne:** SCR/UDP client'ı (bizimkiyle **aynı protokol**) üzerinde **ayrık (tabular) Q-learning** ile şerit takibi.
Python 2, pandas. Karavolos'un "Q-learning with heuristic exploration" tezine dayanıyor.

### 4.1 Dosya akışı
```
pyclient.py (UDP döngüsü, argparse --port vb.)
  └─ driver.Driver.drive(msg)
       ├─ carState.setFromMsg  (msgParser ile sensörleri ayrıştır)
       ├─ GetState2.State(speed, track, trackPos) → 11 bitlik durum
       ├─ RewardFunction.FindQmaxIndex / ComputeReward
       ├─ ActionSelection.Selectaction  (heuristic / random / greedy)
       ├─ GetAccSteer.AccelSteer        (aksiyonu 0..14 indeksine çevir)
       └─ Qtable.update                 (Q-learning güncellemesi)
```

### 4.2 Durum (2048 durum = 11 bit)
- **Hız** 16 kovaya (4 bit): 0,20,40,80,85…130,140,160 — 80–130 arası ince çözünürlük.
- **En uzun mesafe sensörünün yönü** (3 bit): track[5] (−40°), ort(6,7,8), track[9] (0°), ort(10,11,12), track[13] (+40°).
  Pist dışıysa trackPos işaretine göre `000`/`111`.
- **O sensörün mesafesi** 16 kovaya (4 bit).
- Not: `trackPos` ve `angle` duruma **girmiyor** (sadece ödülde) → bilgi kaybı.

### 4.3 Aksiyon (15)
{gaz 1, boş 0, fren −1} × direksiyon {0.5, 0.1, 0, −0.1, −0.5}. Vites kuralla (rpm tabanlı).

### 4.4 Keşif politikası
- `η` olasılıkla **heuristic** (klasik sürücü: `steer=(angle−0.5·trackPos)/0.785`, sensörlerden hedef hız),
- `ε=0.2` olasılıkla **rastgele**,
- kalanı **greedy (Q-max)**. `η = 0.1 − 3e-7·adım` → ~333k adımda heuristic etkisi biter.
- Heuristic aksiyonu da ayrıklaştırılıp tabloya işleniyor → **"öğretmen değil rehber"** yaklaşımı.

### 4.5 Ödül
```
|trackPos| ≥ 0.98 → pist dışı: −|trackPos| (≥1.5 ise −1.5)
|trackPos| ≥ 0.75 → yarım ödül
sıkışma (25 tick |angle|≥45 & v<10, ya da v<3) → −2 ve meta=1 (restart)
normal: 0.05·(v/160)^4 + 0.7·(1/(|pos|+1))^4 + 0.25·(1/(|angle|/40+1))^4
```
→ Ağırlığın %70'i **merkezde kalmak**; hız ödülü çok küçük → **yavaş ama güvenli** şerit takibi öğrenir (yarış için değil).

### 4.6 Güncelleme
`Q(s,a) ← Q(s,a) + 0.01·(r + 0.99·max Q(s',·) − Q(s,a))`, tablo restart/shutdown'da CSV'ye yazılıyor.

### 4.7 Tespit edilen sorunlar
1. **Python 2** (`print x`, `except socket.error, msg`, `execfile`) → Python 3'e port gerekir.
2. Repo'daki `Qtable.csv` **tamamen sıfır** (2048/2048 durum boş) → eğitilmiş model **yok**.
3. Yollar `../input_path/Qtable.csv`, `episode.txt` → repoda olmayan klasör.
4. `pyclient.py` ilk satırında hatalı `2` karakteri var; restart'ta `execfile` ile kendini özyinelemeli çağırıyor.
5. `GetState2.DiscDist` iki kez tanımlı (ikincisi geçerli). Durum indeksi her adımda regex + pandas `.loc`
   ile hesaplanıyor → 50 Hz'de yavaş; numpy dizisi ile değiştirilmeli.
6. `FindQmaxIndex` beraberlikte hep ilk aksiyonu seçiyor (yeni durumda hep "sol + gaz").

### 4.8 Bizim projeye uygunluğu
- ✅ Protokol aynı → mantık doğrudan bir `drive_*` fonksiyonuna taşınabilir.
- ✅ **Heuristic-guided exploration** fikri değerli: mevcut `drive_modular` rehber politika olabilir.
- ⚠️ Tabular Q-learning hız ve kalite olarak yarışma için zayıf; şerit takibi ≠ hızlı tur.

---

## 5. Agent nasıl geliştirilebilir? (yaklaşımlar, kolaydan zora)

### Seviye 1 — Parametre ayarı (mevcut `drive_modular`)
RaceRunner'ın practice modundaki 6 parametreyi pist bazında ayarlamak. En hızlı kazanç ama tavanı düşük.

### Seviye 2 — Daha akıllı kural tabanlı sürücü (önerilen ilk adım)
Aynı iskelette yeni bir `drive_*`:
- **Viraja göre hedef hız:** `target = f(track[9], max(track[8..10]))` — öndeki boş mesafe kısaldıkça
  hızı düşür, fren mesafesine göre **viraja girmeden önce** fren yap.
- **Yarış çizgisi:** en uzun sensör yönüne doğru dümen (A-Raafat'ın 3-bit fikri), virajdan önce dışa açıl.
- **rpm tabanlı vites**, **ABS** (tekerlek kilitlenince fren azalt), mevcut TCS.
- **Direksiyon yumuşatma** (rate limit) — rlTORCS'un kademeli aksiyon fikri.
- **Sıkışma kurtarma:** geri vites + ters direksiyon.
- **Rakip farkındalığı:** `opponents` ile öndeki araca göre şerit değiştir / fren.

### Seviye 3 — Parametre optimizasyonu (kara kutu)
Seviye 2 sürücüsünün ~10–20 parametresini **CMA-ES / Bayesian optimizasyon / genetik algoritma** ile
tur süresi + hasar cezasını minimize edecek şekilde optimize etmek. Her değerlendirme bir yarış (practice)
→ birden çok scr_server portunda paralel koşturulabilir. RL'den çok daha veri-verimli, yarışma için en pratik yol.

### Seviye 4 — Pekiştirmeli öğrenme (düşük boyutlu sensörler)
- Gözlem: `angle, trackPos, speedX/Y, track[19], wheelSpinVel[4], rpm` (normalize, ~29 boyut).
- Aksiyon: sürekli `steer`, `accel/brake` (vites/ABS/TCS kuralla).
- Algoritma: **SAC / TD3 / PPO** (stable-baselines3) — DDPG'nin TORCS'ta çalıştığı biliniyor (Ben Lau).
- Ödül: `v·cos(angle) − v·|sin(angle)| − v·|trackPos|` (+ hasar/pist dışı cezası, pist dışında episode sonu).
- Gerekenler: Windows'ta çalışan bir **Gym wrapper** (gym_torcs.py Linux'a özel; `pkill/xte` yerine
  `meta=1` ile restart ve TORCS'u bir kez açık tutma). Bellek sızıntısı için periyodik TORCS yeniden başlatma.
- **Heuristic ile ısınma:** Seviye 2 sürücüsünden **imitation learning (behavior cloning)** ile başlatıp
  RL ile ince ayar (A-Raafat'ın "rehber heuristic" fikrinin modern hali).

### Seviye 5 — Görsel RL (rlTORCS tarzı)
Yarışma sensör tabanlı olduğu ve Windows'ta derleme gerektirdiği için **önerilmez**.

---

## 6. Önerilen yol haritası

1. **Mevcut dosyaları koru.** Yeni agent'ı `torcs_jm_par.py`'ın **kopyası** olarak (ör. `agents/` altında yeni dosya)
   yaz; `REQUIRED` blokları ve `--port` / `--parameters` sözleşmesini aynen koru.
2. Seviye 2 kural tabanlı sürücüyü yaz, tek araçla (Quick Race'te yalnız `scr_server 1`) test et.
3. Tur süresi / hasar / pist dışı sayısını loglayan basit bir değerlendirme betiği.
4. Seviye 3 optimizasyon ile pist bazlı parametre ayarı.
5. Zaman kalırsa Seviye 4: Windows uyumlu gym wrapper + SAC, Seviye 2 sürücüsünden BC ile başlatma.

## 7. Notlar / uyarılar
- Klonlanan iki repo kendi `.git` klasörünü içeriyor; ana repoya `git add` edilirse **gömülü repo**
  olarak görünür. GitHub'a gönderilmeden önce ya `.gitignore`'a eklenmeli ya da submodule yapılmalı.
- `gym_torcs.py` ve `torcs_jm_par.py` içindeki "relaunch" kodu Linux komutları (`pkill`, `sh autostart.sh`) çağırır;
  Windows'ta zararsızdır ama çalışmaz.
- `snakeoil3_gym.py` 422/424. satırlardaki `SyntaxWarning` zararsız (ASCII sanat string'i).
