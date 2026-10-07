# SABAH 2026-10-07 — ÖNCE SABAH_RAPORU_2.md OKU
- Yeni şampiyon: rl/snapshots/v6g_best.pt (TCS 5.0, kenar 0.9). Teslim: submission/torcs_jm_par_rl_v6g.py →
  79,796 s / 0 hasar, 20/20 + 10/10 hasarsız. Henüz gerçek GUI'de denenmedi.
- Eski şampiyon dosyası submission/torcs_jm_par_rl.py (81,73 s GUI'de doğrulandı) değişmedi.
- v6 modelleri için agent: agents/sac_agent_v6.py (--tcs-th 5.0); select_models --tcs-th 5.0.

# SABAH 2026-10-06 — ÖNCE SABAH_RAPORU.md OKU
- Şampiyon: rl/snapshots/v4d_v02537_best.pt (81,90 s, 0 hasar, 40/40). Teslim: submission/torcs_jm_par_rl.py (doğrulandı).
- Alternatif hızlı/riskli: v4e_v00248 (80,67 s, ~8/10). v4f seçildi: en iyi 9/10, 82,75 s (şampiyonu geçmedi).
- Sıradaki: kullanıcı GUI Corkscrew testi; teslim biçimi; v4f seçim; gerekirse yeni tohumlarla v4d tarifi.

# GECE (2026-10-05 22:40 → 07:00) — otonom çalışma, plan: GECE_PLANI.md, sonuç: SABAH_RAPORU.md
- v4 (yumuşak zikzak cezası) çalışıyor: 3 dk testte zikzak 8,6 → 0,7 yön değişimi/s, tur 84,2 s.
- Tespit: hızı asıl sınırlayan politika — düzde bile pedal ort. %43 (temkinli). v4b'de +%50 ilerleme ödülü.
- 22:45 başladı (3 saat): v4a (idx 1-4), v4b --c-speed 0.25 (idx 5-8), ikisi de v2_ft/final_full'dan.
- Teslim dosyası hazır: submission/torcs_jm_par_rl.py (build_submission.py ile üretilir; orijinal dokunulmadı).
  numpy: 85,704 s / 0 hasar; eğitim yükü altında GUI zaman. 4/5 hasarsız. Saf Python: doğru ama 3,65 ms/adım,
  yük altında 10 ms'yi kaçırıyor (resmi kurulum rehberi numpy kurduruyor → numpy modu geçerli).

# Kaldığımız yer — 2026-10-05 ~15:50

Teslim: **11 Ekim** (Corkscrew, 1 tur, en hızlı + sıfır hasar).

## Doğrulananlar
- Hızlı mod (`wtorcs -r`) = gerçek GUI. İki bağımsız GUI testi:
  - snakeoil3_gym, E-Track 4: GUI 113,69 s / 1585 hasar / 302 km/h ↔ hızlı mod 113,698 s / 1585 / 302,3
  - RL v2 modeli, E-Track 4: GUI 130,346 s / 0 hasar / 241 ↔ hızlı mod 130,356 s / 0 / 241,4
- GUI modunda TORCS lastLapTime göndermiyor → racelog.py son curLapTime ile bitişi tespit ediyor (düzeltildi).

## En iyi model şu an
`rl/snapshots/v2_ft_v05581_best.pt` + **`agents/sac_agent_v2.py`** (ısınma + kuyruk boşaltma)
- Corkscrew deterministik: **85,736 s, 0 hasar** (skor tablosunda #1)
- GUI zamanlaması ×10: 10/10 bitiş, 9/10 hasarsız; 0 kaçan adımda hep 85,736 s
- Sorun: düz yolda zikzak (hız>150'de saniyede ~9 yön değişimi, ort gaz %54) → hız kaybı
- sac_agent.py (v1) bu modelle 2/10: başta kaçan adımlar kalıcı gecikme yaratıyordu → v2 agent bunu çözdü.

## 2026-10-05 ~16:50 güncellemesi — çalışan süreç YOK
- v3 (sert direksiyon hız sınırı) BAŞARISIZ: v3_ft_1h ve v3_ft_strong_1h (STOP ile güvenle kapatıldı, final.pt kayıtlı)
  0 tur; araç ~400-500 m (ilk sert fren virajı) ve ~2400-2470 m (corkscrew S virajı) noktalarında pistten çıkıyor.
  Sebep: 200 km/h'te adım başına 0.04 sınırı, hızlı direksiyon gereken virajları imkânsız kılıyor.
- **Şampiyon hâlâ v2:** rl/snapshots/v2_ft_v05581_best.pt + agents/sac_agent_v2.py (85,736 s, 0 hasar).
- SIRADAKİ = v4 (akşam büyük eğitim): sert sınır yok; zikzak sadece ödülle cezalandırılır
  (direksiyon yön değiştirme cezası + önü açıkken/düzde büyük direksiyon cezası). v2_ft/final_full.pt'den devam.
  Önce kısa testle 450 m ve 2470 m virajlarını geçebildiğini doğrula.
- Yeni: eğitim klasörüne `STOP` dosyası → güvenli kapanış. Telemetri artık koşu sırasında diske yazılıyor.
- Kaybolan Corkscrew GUI testi: terminal penceresi kapatıldığı için (window-CLOSE) veri yok; tekrar yapılacak.

## (eski) Çalışan / sıradaki
- 15:50'de başladı, ~17:50 biter: `v3_ft` ve `v3_ft_strong` (torcs_env_v3: direksiyon hız sınırı + zikzak cezası,
  v2_ft/final_full.pt'den devam). Agent: `agents/sac_agent_v3.py`.
- Bitince: `python racelab/rl/select_models.py --run v3_ft --env v3 --top 20 --repeat 10 --procs 6 --idx-from 1`
  (aynısı v3_ft_strong), sonra en iyisini run_benchmark ile sac_agent_v3 üzerinden skor tablosuna yaz ve GUI'de Corkscrew testi.
- Teslim dosyası: torcs_jm_par.py iskeleti (REQUIRED bloklar) + numpy'ye gömülü ağırlıklar, PyTorch'suz. (henüz yapılmadı)
