# Lap Log — skor tablosu

Otomatik üretilir (`racelab/run_benchmark.py`). Ham veri: `leaderboard.csv`,
her koşunun telemetrisi: `runs/<run_id>/telemetry.csv`.

Sıralama: önce turu bitirenler (hasarsız olan önde, sonra tur süresi),
sonra bitiremeyenler (en uzağa giden önde). Pist: Corkscrew ≈ 3608 m.
`@gui-timing` = TORCS'un GUI'deki 10 ms bekleme süresiyle koşu (gerçek koşula yakın, rastgelelik var).

## Her agent'ın en iyi koşusu

| # | Agent (label) | Bitirme | Tur süresi (s) | Mesafe (m) | Hasar | Çarpma | Pist dışı (kez / s) | Max hız | Ort. hız | Koşu |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | sac_g995_best(53dk)@gui-timing | 2/10 | 103.642 | 3633.1 | 0 | 0 | 0 / 0.0 | 223.2 | 124.1 | `20261004-191543_sac_g995_best(53dk)@gui-timing` |
| 2 | snakeoil3_gym#etrack4 | 2/2 | 113.698 | 7095.5 | 1585 | 7 | 5 / 36.02 | 302.3 | 226.2 | `20261004-180550_snakeoil3_gym#etrack4` |
| 3 | snakeoil3_gym#etrack4@gui-timing | 4/5 | 117.944 | 7076.0 | 1754 | 8 | 5 / 41.46 | 302.5 | 217.8 | `20261004-180558_snakeoil3_gym#etrack4@gui-timing` |
| 4 | snakeoil3_gym@gui-timing | 4/25 | 134.16 | 3692.8 | 3410 | 7 | 6 / 79.3 | 247.3 | 98.7 | `20261004-180458_snakeoil3_gym@gui-timing` |
| 5 | snakeoil3_jm2@gui-timing | 1/5 | 308.23 | 3708.5 | 2680 | 8 | 8 / 90.08 | 238.8 | 36.8 | `20261004-175923_snakeoil3_jm2@gui-timing` |
| 6 | snakeoil3_jm2 | 0/2 | DNF | 3298.2 | 2921 | 8 | 7 / 399.16 | 232.7 | 26.9 | `20261004-175844_snakeoil3_jm2` |
| 7 | torcs_jm_par | 0/2 | DNF | 2511.4 | 242 | 3 | 5 / 348.44 | 101.8 | 19.7 | `20261004-180024_torcs_jm_par` |
| 8 | torcs_jm_par@gui-timing | 0/5 | DNF | 2483.4 | 247 | 3 | 6 / 360.56 | 102.9 | 19.6 | `20261004-180051_torcs_jm_par@gui-timing` |
| 9 | sac_g995_final(60dk) | 0/2 | DNF | 2471.4 | 399 | 1 | 1 / 387.86 | 253.3 | 19.4 | `20261004-191831_sac_g995_final(60dk)` |
| 10 | snakeoil3_gym | 0/2 | DNF | 2470.6 | 1863 | 5 | 5 / 410.88 | 237.9 | 20.5 | `20261004-175755_snakeoil3_gym` |
| 11 | sac_g995_final(60dk)@gui-timing | 0/10 | DNF | 1727.2 | 0 | 0 | 1 / 394.38 | 225.7 | 13.3 | `20261004-192003_sac_g995_final(60dk)@gui-timing` |
| 12 | sac_g995_best(53dk) | 0/2 | DNF | 498.3 | 217 | 1 | 1 / 427.38 | 231.7 | 4.0 | `20261004-191241_sac_g995_best(53dk)` |
| 13 | jmcncarai | 0/2 | DNF | 497.8 | 274 | 2 | 1 / 426.3 | 161.7 | 3.7 | `20261004-175935_jmcncarai` |
| 14 | jmcncarai@gui-timing | 0/5 | DNF | 497.7 | 274 | 2 | 1 / 426.3 | 161.7 | 3.7 | `20261004-175956_jmcncarai@gui-timing` |
| 15 | sac_smoke2(3dk) | 0/1 | DNF | 489.2 | 133 | 1 | 1 / 427.52 | 243.0 | 4.0 | `20261004-181753_sac_smoke2(3dk)` |

## Tüm koşular (yeniden eskiye)

| Zaman | Label | Tur (s) | Mesafe (m) | Hasar | Çarpma | Pist dışı | Max hız | Mod | Not |
|---|---|---|---|---|---|---|---|---|---|
| 20261004-192033 | sac_g995_final(60dk)@gui-timing | DNF | 185.7 | 816 | 1 | 2 | 129.2 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-192023 | sac_g995_final(60dk)@gui-timing | DNF | 993.3 | 0 | 0 | 2 | 225.7 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-192013 | sac_g995_final(60dk)@gui-timing | DNF | 117.6 | 8 | 1 | 1 | 88.8 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-192003 | sac_g995_final(60dk)@gui-timing | DNF | 1727.2 | 0 | 0 | 1 | 225.7 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191953 | sac_g995_final(60dk)@gui-timing | DNF | 959.7 | 32 | 1 | 1 | 210.0 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191943 | sac_g995_final(60dk)@gui-timing | DNF | 1023.2 | 0 | 0 | 2 | 189.9 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191933 | sac_g995_final(60dk)@gui-timing | DNF | 1111.9 | 60 | 1 | 1 | 226.0 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191922 | sac_g995_final(60dk)@gui-timing | DNF | 412.4 | 283 | 1 | 1 | 157.1 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191912 | sac_g995_final(60dk)@gui-timing | DNF | 997.2 | 1 | 1 | 1 | 225.7 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191902 | sac_g995_final(60dk)@gui-timing | DNF | 1353.9 | 192 | 1 | 2 | 225.7 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191846 | sac_g995_final(60dk) | DNF | 2471.4 | 399 | 1 | 1 | 253.3 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191831 | sac_g995_final(60dk) | DNF | 2471.4 | 399 | 1 | 1 | 253.3 | fast | 1 saat eğitim sonu, gamma .995 |
| 20261004-191611 | sac_g995_best(53dk)@gui-timing | 171.85 | 3619.9 | 0 | 0 | 4 | 221.9 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191551 | sac_g995_best(53dk)@gui-timing | DNF | 498.3 | 217 | 1 | 1 | 231.7 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191543 | sac_g995_best(53dk)@gui-timing | 103.642 | 3633.1 | 0 | 0 | 0 | 223.2 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191526 | sac_g995_best(53dk)@gui-timing | DNF | 1558.5 | 0 | 0 | 1 | 223.6 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191508 | sac_g995_best(53dk)@gui-timing | DNF | 1587.9 | 0 | 0 | 1 | 222.6 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191450 | sac_g995_best(53dk)@gui-timing | DNF | 498.3 | 217 | 1 | 1 | 231.7 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191432 | sac_g995_best(53dk)@gui-timing | DNF | 2921.0 | 0 | 0 | 1 | 228.2 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191415 | sac_g995_best(53dk)@gui-timing | DNF | 499.9 | 224 | 1 | 1 | 231.7 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191357 | sac_g995_best(53dk)@gui-timing | DNF | 1590.4 | 0 | 0 | 1 | 226.8 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191340 | sac_g995_best(53dk)@gui-timing | DNF | 1033.4 | 0 | 0 | 1 | 226.7 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191312 | sac_g995_best(53dk) | DNF | 498.3 | 217 | 1 | 1 | 231.7 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-191241 | sac_g995_best(53dk) | DNF | 498.3 | 217 | 1 | 1 | 231.7 | fast | eğitim sürerken alınan best.pt kopyası |
| 20261004-181753 | sac_smoke2(3dk) | DNF | 489.2 | 133 | 1 | 1 | 243.0 | fast | 3 dk smoke eğitim, gamma .99 |
| 20261004-180619 | snakeoil3_gym#etrack4@gui-timing | 122.004 | 7071.5 | 1924 | 7 | 5 | 302.1 | fast | E-Track 4, GUI zamanlaması |
| 20261004-180616 | snakeoil3_gym#etrack4@gui-timing | 187.898 | 7074.9 | 2016 | 12 | 9 | 302.3 | fast | E-Track 4, GUI zamanlaması |
| 20261004-180608 | snakeoil3_gym#etrack4@gui-timing | DNF | 4912.2 | 1465 | 39 | 12 | 281.1 | fast | E-Track 4, GUI zamanlaması |
| 20261004-180602 | snakeoil3_gym#etrack4@gui-timing | 508.938 | 7116.7 | 1680 | 17 | 15 | 276.0 | fast | E-Track 4, GUI zamanlaması |
| 20261004-180558 | snakeoil3_gym#etrack4@gui-timing | 117.944 | 7076.0 | 1754 | 8 | 5 | 302.5 | fast | E-Track 4, GUI zamanlaması |
| 20261004-180553 | snakeoil3_gym#etrack4 | 113.698 | 7095.5 | 1585 | 7 | 5 | 302.3 | fast | E-Track 4, deterministik |
| 20261004-180550 | snakeoil3_gym#etrack4 | 113.698 | 7095.5 | 1585 | 7 | 5 | 302.3 | fast | E-Track 4, deterministik |
| 20261004-180528 | snakeoil3_gym@gui-timing | DNF | 549.0 | 463 | 3 | 1 | 242.9 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180523 | snakeoil3_gym@gui-timing | DNF | 2061.8 | 757 | 5 | 4 | 245.2 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180518 | snakeoil3_gym@gui-timing | DNF | 543.5 | 453 | 2 | 1 | 241.7 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180512 | snakeoil3_gym@gui-timing | DNF | 2472.4 | 1236 | 4 | 4 | 237.1 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180506 | snakeoil3_gym@gui-timing | DNF | 2048.1 | 791 | 5 | 4 | 245.2 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180501 | snakeoil3_gym@gui-timing | DNF | 543.5 | 488 | 2 | 1 | 246.6 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180458 | snakeoil3_gym@gui-timing | 134.16 | 3692.8 | 3410 | 7 | 6 | 247.3 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180452 | snakeoil3_gym@gui-timing | DNF | 2082.3 | 876 | 5 | 4 | 246.7 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180445 | snakeoil3_gym@gui-timing | DNF | 3366.5 | 2087 | 8 | 8 | 237.9 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180439 | snakeoil3_gym@gui-timing | DNF | 2470.7 | 1983 | 5 | 5 | 237.9 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180436 | snakeoil3_gym@gui-timing | 135.152 | 3651.5 | 2166 | 7 | 8 | 245.6 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180433 | snakeoil3_gym@gui-timing | 142.234 | 3695.3 | 2201 | 8 | 8 | 245.6 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180427 | snakeoil3_gym@gui-timing | DNF | 2088.0 | 664 | 6 | 4 | 241.8 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180421 | snakeoil3_gym@gui-timing | DNF | 2054.8 | 821 | 5 | 4 | 244.4 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180415 | snakeoil3_gym@gui-timing | DNF | 575.7 | 419 | 2 | 1 | 233.5 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180409 | snakeoil3_gym@gui-timing | DNF | 2043.0 | 856 | 5 | 3 | 245.6 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180405 | snakeoil3_gym@gui-timing | 142.02 | 3620.5 | 1950 | 7 | 7 | 237.9 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180359 | snakeoil3_gym@gui-timing | DNF | 2470.6 | 1973 | 5 | 5 | 237.9 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180354 | snakeoil3_gym@gui-timing | DNF | 2072.8 | 830 | 6 | 4 | 245.2 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180348 | snakeoil3_gym@gui-timing | DNF | 2091.6 | 850 | 5 | 3 | 246.7 | fast | baseline, GUI zamanlaması, bitirme oranı testi |
| 20261004-180109 | torcs_jm_par@gui-timing | DNF | 2467.4 | 277 | 3 | 4 | 102.5 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180103 | torcs_jm_par@gui-timing | DNF | 532.1 | 50 | 2 | 1 | 103.2 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180057 | torcs_jm_par@gui-timing | DNF | 2478.8 | 227 | 2 | 5 | 107.4 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180051 | torcs_jm_par@gui-timing | DNF | 2483.4 | 247 | 3 | 6 | 102.9 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180045 | torcs_jm_par@gui-timing | DNF | 550.1 | 39 | 2 | 1 | 104.5 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180034 | torcs_jm_par | DNF | 2511.4 | 242 | 3 | 5 | 101.8 | fast | baseline, deterministik (-t 1s) |
| 20261004-180024 | torcs_jm_par | DNF | 2511.4 | 242 | 3 | 5 | 101.8 | fast | baseline, deterministik (-t 1s) |
| 20261004-180018 | jmcncarai@gui-timing | DNF | 493.4 | 221 | 2 | 1 | 163.1 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180013 | jmcncarai@gui-timing | DNF | 479.1 | 335 | 4 | 1 | 163.7 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180007 | jmcncarai@gui-timing | DNF | 495.5 | 199 | 2 | 1 | 163.2 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-180002 | jmcncarai@gui-timing | DNF | 493.9 | 228 | 3 | 1 | 163.1 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175956 | jmcncarai@gui-timing | DNF | 497.7 | 274 | 2 | 1 | 161.7 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175945 | jmcncarai | DNF | 497.8 | 274 | 2 | 1 | 161.7 | fast | baseline, deterministik (-t 1s) |
| 20261004-175935 | jmcncarai | DNF | 497.8 | 274 | 2 | 1 | 161.7 | fast | baseline, deterministik (-t 1s) |
| 20261004-175928 | snakeoil3_jm2@gui-timing | DNF | 2468.7 | 2384 | 5 | 5 | 240.7 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175923 | snakeoil3_jm2@gui-timing | 308.23 | 3708.5 | 2680 | 8 | 8 | 238.8 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175917 | snakeoil3_jm2@gui-timing | DNF | 2120.8 | 813 | 6 | 4 | 251.6 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175912 | snakeoil3_jm2@gui-timing | DNF | 2468.7 | 2454 | 6 | 6 | 251.7 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175905 | snakeoil3_jm2@gui-timing | DNF | 2468.7 | 2715 | 7 | 6 | 251.5 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175854 | snakeoil3_jm2 | DNF | 3298.2 | 2921 | 8 | 7 | 232.7 | fast | baseline, deterministik (-t 1s) |
| 20261004-175844 | snakeoil3_jm2 | DNF | 3298.2 | 2921 | 8 | 7 | 232.7 | fast | baseline, deterministik (-t 1s) |
| 20261004-175839 | snakeoil3_gym@gui-timing | DNF | 543.5 | 603 | 2 | 1 | 247.3 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175833 | snakeoil3_gym@gui-timing | DNF | 2084.0 | 772 | 5 | 4 | 238.1 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175827 | snakeoil3_gym@gui-timing | DNF | 3377.8 | 3145 | 7 | 8 | 245.6 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175822 | snakeoil3_gym@gui-timing | DNF | 2065.8 | 671 | 5 | 4 | 237.9 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175816 | snakeoil3_gym@gui-timing | DNF | 2470.7 | 1751 | 5 | 5 | 243.3 | fast | baseline, GUI zamanlaması (-t 10ms) |
| 20261004-175805 | snakeoil3_gym | DNF | 2470.6 | 1863 | 5 | 5 | 237.9 | fast | baseline, deterministik (-t 1s) |
| 20261004-175755 | snakeoil3_gym | DNF | 2470.6 | 1863 | 5 | 5 | 237.9 | fast | baseline, deterministik (-t 1s) |
