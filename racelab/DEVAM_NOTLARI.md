# Kaldığımız yer — 2026-10-04

Çalışan süreç yok; her şey diskte. Teslim: **11 Ekim** (Corkscrew, 1 tur, en hızlı + sıfır hasar).

## Şu ana kadar
- Benchmark + skor tablosu hazır: `results/LAP_LOG.md`. Mevcut agent'lar Corkscrew'u güvenilir bitiremiyor
  (en iyi: snakeoil3_gym 4/25 bitiş, 134 s, ~2000 hasar). E-Track 4'te snakeoil3_gym 113,7 s.
- RL (SAC), 1 saatlik iki eğitim:
  - `rl/runs/sac_g990` (gamma 0.99): 460 m virajını hiç geçemedi → başarısız.
  - `rl/runs/sac_g995` (gamma 0.995): 1461 eğitim turu tamamladı, hepsi hasarsız; en iyi tur 86,0 s
    (eval turu 45 kez). **Ama kaydedilen modeller bunu yarış koşulunda tekrarlayamıyor:**
    - `snapshots/sac_g995_best_at53min.pt` → GUI zamanlamasıyla 2/10 hasarsız bitiş (103,6 s ve 171,9 s)
    - `rl/runs/sac_g995/final.pt` → 0/10 bitiş, deterministik koşuda 2471 m'de çarpma

## Neden: tespit edilen sorunlar
1. **best.pt hatası:** `train_sac.py` best.pt'ye eval'i yapan sürümü değil, sonucun geldiği andaki
   daha yeni ağırlıkları kaydediyor → 86–88 s'lik modeller kayboldu.
2. Politika eğitim boyunca dalgalanıyor (SAC'te normal); son ağırlık en iyisi değil.
3. GUI zamanlamasında (10 ms) gecikmeler politikayı eğitimde görmediği durumlara sokuyor.

## Sıradaki adımlar (yeni dosyalarla: `train_sac_v2.py` vb.)
1. Eval'i yapan sürümün ağırlıklarını kaydet. Eval politikası olarak her yayında versiyonlu kopya tut.
2. Model seçimi: aday modeller GUI zamanlamasıyla ×10 koşturulsun; **hasarsız bitirme oranı → tur süresi**.
3. Çarpmama odaklı ödül: `|trackPos| > 0.8` için kademeli ceza, hıza bağlı pist dışı cezası.
4. Sağlamlık: eğitimde rastgele aksiyon gecikmesi / ara sıra adım tekrarı (GUI zamanlamasına alışsın).
5. Mevcut sac_g995 ağırlıklarından devam etme seçeneği (`final_full.pt` actor+critic içeriyor; replay buffer kayıtlı değil).

## Devam komutları (proje kökünden)
```powershell
python racelab/run_benchmark.py --agent racelab/agents/sac_agent.py --label X --model racelab/rl/snapshots/sac_g995_best_at53min.pt --udp-timeout-us 10000 --repeat 10
```
