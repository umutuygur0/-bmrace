# Lap Log — skor tablosu

Otomatik üretilir (`racelab/run_benchmark.py`). Ham veri: `leaderboard.csv`,
her koşunun telemetrisi: `runs/<run_id>/telemetry.csv`.

Sıralama: önce turu bitirenler, sonra hasarsızlar, sonra tur süresi.

## Her agent'ın en iyi koşusu

| # | Agent (label) | Tur süresi (s) | Hasar | Çarpma | Pist dışı (kez / s) | Max hız | Ort. hız | Bitirdi | Mod | Koşu |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | snakeoil3_gym | 445.346 | 847 | 5 | 4 / 416.72 | 247.3 | 16.4 | ✅ | fast | `20261004-175452_snakeoil3_gym` |
| 2 | snakeoil3_jm2 | 445.346 | 811 | 5 | 5 / 408.78 | 242.4 | 16.0 | ✅ | fast | `20261004-175510_snakeoil3_jm2` |
| 3 | jmcncarai | 445.346 | 274 | 2 | 1 / 426.3 | 161.7 | 3.7 | ✅ | fast | `20261004-175534_jmcncarai` |
| 4 | torcs_jm_par | 445.346 | 449 | 5 | 9 / 325.84 | 105.2 | 19.8 | ✅ | fast | `20261004-175547_torcs_jm_par` |

## Tüm koşular (yeniden eskiye)

| Zaman | Label | Tur (s) | Hasar | Çarpma | Pist dışı | Max hız | Bitirdi | Mod | Not |
|---|---|---|---|---|---|---|---|---|---|
| 20261004-175559 | torcs_jm_par | 445.346 | 329 | 2 | 7 | 102.0 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175552 | torcs_jm_par | 445.346 | 357 | 4 | 11 | 101.9 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175547 | torcs_jm_par | 445.346 | 449 | 5 | 9 | 105.2 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175540 | jmcncarai | 445.346 | 214 | 2 | 1 | 162.8 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175534 | jmcncarai | 445.346 | 274 | 2 | 1 | 161.7 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175528 | jmcncarai | 446.566 | 318 | 7 | 1 | 162.3 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175521 | snakeoil3_jm2 | 445.346 | 2417 | 6 | 5 | 252.0 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175515 | snakeoil3_jm2 | 445.346 | 3136 | 7 | 6 | 249.6 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175510 | snakeoil3_jm2 | 445.346 | 811 | 5 | 5 | 242.4 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175503 | snakeoil3_gym | 445.346 | 820 | 4 | 4 | 245.2 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175458 | snakeoil3_gym | 445.346 | 806 | 5 | 4 | 246.7 | ✅ | fast | baseline (orijinal, dokunulmadı) |
| 20261004-175452 | snakeoil3_gym | 445.346 | 847 | 5 | 4 | 247.3 | ✅ | fast | baseline (orijinal, dokunulmadı) |
