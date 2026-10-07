# Lap Log — skor tablosu

Otomatik üretilir (`racelab/run_benchmark.py`). Ham veri: `leaderboard.csv`,
her koşunun telemetrisi: `runs/<run_id>/telemetry.csv`.

Sıralama: önce turu bitirenler (hasarsız olan önde, sonra tur süresi),
sonra bitiremeyenler (en uzağa giden önde). Pist: Corkscrew ≈ 3608 m.
`@gui-timing` = TORCS'un GUI'deki 10 ms bekleme süresiyle koşu (gerçek koşula yakın, rastgelelik var).

## Her agent'ın en iyi koşusu

| # | Agent (label) | Bitirme | Tur süresi (s) | Mesafe (m) | Hasar | Çarpma | Pist dışı (kez / s) | Max hız | Ort. hız | Koşu |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SUBMISSION_v6g@GUI | 1/1 | 79.782 | 3617.7 | 0 | 0 | 0 / 0.0 | 264.2 | 159.6 | `20261007-101531_SUBMISSION_v6g@GUI` |
| 2 | SUBMISSION_v6g@gui-timing | 10/10 | 79.788 | 3632.9 | 0 | 0 | 0 / 0.0 | 264.2 | 159.8 | `20261007-073420_SUBMISSION_v6g@gui-timing` |
| 3 | SUBMISSION_v6g | 1/1 | 79.796 | 3632.4 | 0 | 0 | 0 / 0.0 | 264.2 | 159.8 | `20261007-073415_SUBMISSION_v6g` |
| 4 | SUBMISSION_v6f_fast | 1/1 | 79.806 | 3631.6 | 0 | 0 | 0 / 0.0 | 254.6 | 160.8 | `20261007-064252_SUBMISSION_v6f_fast` |
| 5 | SUBMISSION_v6f_fast@gui-timing | 4/10 | 79.806 | 3631.6 | 0 | 0 | 0 / 0.0 | 254.6 | 160.8 | `20261007-064306_SUBMISSION_v6f_fast@gui-timing` |
| 6 | sac_v6f_best | 1/1 | 79.864 | 3628.1 | 0 | 0 | 0 / 0.0 | 254.7 | 160.6 | `20261007-064208_sac_v6f_best` |
| 7 | sac_v4e_v00248(hızlı-riskli) | 1/1 | 80.668 | 3693.8 | 0 | 0 | 0 / 0.0 | 244.3 | 158.8 | `20261006-060619_sac_v4e_v00248(hızlı-riskli)` |
| 8 | sac_v6f_v00879 | 1/1 | 80.696 | 3690.8 | 0 | 0 | 0 / 0.0 | 249.9 | 158.9 | `20261007-064215_sac_v6f_v00879` |
| 9 | sac_v6f_v01759 | 1/1 | 81.056 | 3670.7 | 0 | 0 | 0 / 0.0 | 247.6 | 158.4 | `20261007-064222_sac_v6f_v01759` |
| 10 | sac_v6b_v00249 | 1/1 | 81.182 | 3664.9 | 0 | 0 | 0 / 0.0 | 242.9 | 157.4 | `20261007-022954_sac_v6b_v00249` |
| 11 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 8/10 | 81.248 | 3662.7 | 0 | 0 | 0 / 0.0 | 245.2 | 157.5 | `20261006-060707_sac_v4e_v00248(hızlı-riskli)@gui-timing` |
| 12 | SUBMISSION_v6c_safe | 1/1 | 81.352 | 3659.0 | 0 | 0 | 0 / 0.0 | 251.1 | 157.5 | `20261007-064400_SUBMISSION_v6c_safe` |
| 13 | SUBMISSION_v6c_safe@gui-timing | 10/10 | 81.352 | 3659.0 | 0 | 0 | 0 / 0.0 | 251.1 | 157.5 | `20261007-064408_SUBMISSION_v6c_safe@gui-timing` |
| 14 | sac_v6c_v01404 | 1/1 | 81.424 | 3654.8 | 0 | 0 | 0 / 0.0 | 251.0 | 157.3 | `20261007-064227_sac_v6c_v01404` |
| 15 | SUBMISSION_v4d@GUI | 2/2 | 81.718 | 3617.7 | 0 | 0 | 0 / 0.0 | 251.0 | 156.1 | `20261007-002313_SUBMISSION_v4d@GUI` |
| 16 | SUBMISSION_v4d(numpy) | 1/1 | 81.736 | 3630.1 | 0 | 0 | 0 / 0.0 | 251.0 | 156.1 | `20261006-015524_SUBMISSION_v4d(numpy)` |
| 17 | SUBMISSION_v4d(numpy)@gui-timing | 10/10 | 81.736 | 3630.1 | 0 | 0 | 0 / 0.0 | 251.0 | 156.1 | `20261006-015536_SUBMISSION_v4d(numpy)@gui-timing` |
| 18 | sac_v4d_v02537 | 2/2 | 81.904 | 3623.0 | 0 | 0 | 0 / 0.0 | 251.2 | 155.8 | `20261006-015359_sac_v4d_v02537` |
| 19 | sac_v4d_v02537[agent_v2]@gui-timing | 10/10 | 82.476 | 3669.4 | 0 | 0 | 0 / 0.0 | 249.5 | 154.2 | `20261006-015452_sac_v4d_v02537[agent_v2]@gui-timing` |
| 20 | SUBMISSION_v4d(saf-python)@gui-timing | 5/5 | 82.544 | 3668.6 | 0 | 0 | 0 / 0.0 | 244.8 | 154.1 | `20261006-015619_SUBMISSION_v4d(saf-python)@gui-timing` |
| 21 | SUBMISSION_v2(numpy)@gui-timing | 4/5 | 85.694 | 3634.1 | 0 | 0 | 0 / 0.0 | 232.1 | 149.2 | `20261005-224718_SUBMISSION_v2(numpy)@gui-timing` |
| 22 | SUBMISSION_v2(numpy) | 1/1 | 85.704 | 3633.2 | 0 | 0 | 0 / 0.0 | 231.8 | 149.1 | `20261005-224646_SUBMISSION_v2(numpy)` |
| 23 | SUBMISSION_v2(saf-python) | 1/1 | 85.704 | 3633.2 | 0 | 0 | 0 / 0.0 | 231.8 | 149.1 | `20261005-224749_SUBMISSION_v2(saf-python)` |
| 24 | sac_v2_ft_v05581 | 2/2 | 85.736 | 3630.9 | 0 | 0 | 0 / 0.0 | 231.0 | 149.1 | `20261005-153101_sac_v2_ft_v05581` |
| 25 | sac_v2_ft_v05581@gui-timing | 2/10 | 85.736 | 3630.9 | 0 | 0 | 0 / 0.0 | 231.0 | 149.1 | `20261005-153157_sac_v2_ft_v05581@gui-timing` |
| 26 | sac_v2_ft_v05581[agent_v2]@gui-timing | 10/10 | 85.736 | 3630.9 | 0 | 0 | 0 / 0.0 | 231.0 | 149.1 | `20261005-153407_sac_v2_ft_v05581[agent_v2]@gui-timing` |
| 27 | sac_v2_ft_v05581[agent_v2] | 1/1 | 85.736 | 3630.9 | 0 | 0 | 0 / 0.0 | 231.0 | 149.1 | `20261005-155629_sac_v2_ft_v05581[agent_v2]` |
| 28 | sac_g995_best | 2/2 | 87.612 | 3635.4 | 0 | 0 | 0 / 0.0 | 249.1 | 145.3 | `20261005-130829_sac_g995_best` |
| 29 | sac_g995_best@gui-timing | 2/10 | 87.612 | 3635.4 | 0 | 0 | 0 / 0.0 | 249.1 | 145.3 | `20261005-131135_sac_g995_best@gui-timing` |
| 30 | sac_g995_best(53dk)@gui-timing | 2/10 | 103.642 | 3633.1 | 0 | 0 | 0 / 0.0 | 223.2 | 124.1 | `20261004-191543_sac_g995_best(53dk)@gui-timing` |
| 31 | sac_v2_ft_v05581@GUI | 2/2 | 130.346 | 7066.1 | 0 | 0 | 2 / 0.34 | 241.4 | 191.8 | `20261005-154146_sac_v2_ft_v05581@GUI` |
| 32 | sac_v2_ft_v05581[agent_v2]#etrack4 | 2/2 | 130.356 | 7162.4 | 0 | 0 | 2 / 0.34 | 241.4 | 191.9 | `20261005-154834_sac_v2_ft_v05581[agent_v2]#etrack4` |
| 33 | snakeoil3_gym#etrack4@GUI | 2/2 | 113.684 | 7065.6 | 1585 | 7 | 5 / 36.02 | 302.3 | 226.0 | `20261005-151545_snakeoil3_gym#etrack4@GUI` |
| 34 | snakeoil3_gym#etrack4 | 2/2 | 113.698 | 7095.5 | 1585 | 7 | 5 / 36.02 | 302.3 | 226.2 | `20261004-180550_snakeoil3_gym#etrack4` |
| 35 | snakeoil3_gym#etrack4@gui-timing | 4/5 | 117.944 | 7076.0 | 1754 | 8 | 5 / 41.46 | 302.5 | 217.8 | `20261004-180558_snakeoil3_gym#etrack4@gui-timing` |
| 36 | snakeoil3_gym@gui-timing | 4/25 | 134.16 | 3692.8 | 3410 | 7 | 6 / 79.3 | 247.3 | 98.7 | `20261004-180458_snakeoil3_gym@gui-timing` |
| 37 | snakeoil3_jm2@gui-timing | 1/5 | 308.23 | 3708.5 | 2680 | 8 | 8 / 90.08 | 238.8 | 36.8 | `20261004-175923_snakeoil3_jm2@gui-timing` |
| 38 | snakeoil3_jm2 | 0/2 | DNF | 3298.2 | 2921 | 8 | 7 / 399.16 | 232.7 | 26.9 | `20261004-175844_snakeoil3_jm2` |
| 39 | SUBMISSION_v2(saf-python)@gui-timing | 0/5 | DNF | 3231.9 | 1 | 1 | 1 / 359.7 | 221.1 | 25.2 | `20261005-225052_SUBMISSION_v2(saf-python)@gui-timing` |
| 40 | torcs_jm_par | 0/2 | DNF | 2511.4 | 242 | 3 | 5 / 348.44 | 101.8 | 19.7 | `20261004-180024_torcs_jm_par` |
| 41 | torcs_jm_par@gui-timing | 0/5 | DNF | 2483.4 | 247 | 3 | 6 / 360.56 | 102.9 | 19.6 | `20261004-180051_torcs_jm_par@gui-timing` |
| 42 | sac_g995_final(60dk) | 0/2 | DNF | 2471.4 | 399 | 1 | 1 / 387.86 | 253.3 | 19.4 | `20261004-191831_sac_g995_final(60dk)` |
| 43 | snakeoil3_gym | 0/2 | DNF | 2470.6 | 1863 | 5 | 5 / 410.88 | 237.9 | 20.5 | `20261004-175755_snakeoil3_gym` |
| 44 | sac_g995_final(60dk)@gui-timing | 0/10 | DNF | 1727.2 | 0 | 0 | 1 / 394.38 | 225.7 | 13.3 | `20261004-192003_sac_g995_final(60dk)@gui-timing` |
| 45 | sac_g995_best(53dk) | 0/2 | DNF | 498.3 | 217 | 1 | 1 / 427.38 | 231.7 | 4.0 | `20261004-191241_sac_g995_best(53dk)` |
| 46 | jmcncarai | 0/2 | DNF | 497.8 | 274 | 2 | 1 / 426.3 | 161.7 | 3.7 | `20261004-175935_jmcncarai` |
| 47 | jmcncarai@gui-timing | 0/5 | DNF | 497.7 | 274 | 2 | 1 / 426.3 | 161.7 | 3.7 | `20261004-175956_jmcncarai@gui-timing` |
| 48 | sac_smoke2(3dk) | 0/1 | DNF | 489.2 | 133 | 1 | 1 / 427.52 | 243.0 | 4.0 | `20261004-181753_sac_smoke2(3dk)` |

## Tüm koşular (yeniden eskiye)

| Zaman | Label | Tur (s) | Mesafe (m) | Hasar | Çarpma | Pist dışı | Max hız | Mod | Not |
|---|---|---|---|---|---|---|---|---|---|
| 20261007-101531 | SUBMISSION_v6g@GUI | 79.782 | 3617.7 | 0 | 0 | 0 | 264.2 | gui |  |
| 20261007-073450 | SUBMISSION_v6g@gui-timing | 80.672 | 3694.6 | 0 | 0 | 0 | 263.9 | fast | CPU boş |
| 20261007-073447 | SUBMISSION_v6g@gui-timing | 80.546 | 3701.0 | 0 | 0 | 0 | 263.8 | fast | CPU boş |
| 20261007-073444 | SUBMISSION_v6g@gui-timing | 80.13 | 3722.0 | 0 | 0 | 0 | 264.3 | fast | CPU boş |
| 20261007-073440 | SUBMISSION_v6g@gui-timing | 80.684 | 3692.6 | 0 | 0 | 0 | 263.7 | fast | CPU boş |
| 20261007-073437 | SUBMISSION_v6g@gui-timing | 80.656 | 3695.5 | 0 | 0 | 0 | 263.7 | fast | CPU boş |
| 20261007-073433 | SUBMISSION_v6g@gui-timing | 80.228 | 3717.3 | 0 | 0 | 0 | 264.5 | fast | CPU boş |
| 20261007-073430 | SUBMISSION_v6g@gui-timing | 80.658 | 3695.3 | 0 | 0 | 0 | 263.7 | fast | CPU boş |
| 20261007-073427 | SUBMISSION_v6g@gui-timing | 80.632 | 3696.6 | 0 | 0 | 0 | 264.1 | fast | CPU boş |
| 20261007-073424 | SUBMISSION_v6g@gui-timing | 80.576 | 3699.5 | 0 | 0 | 0 | 263.9 | fast | CPU boş |
| 20261007-073420 | SUBMISSION_v6g@gui-timing | 79.788 | 3632.9 | 0 | 0 | 0 | 264.2 | fast | CPU boş |
| 20261007-073415 | SUBMISSION_v6g | 79.796 | 3632.4 | 0 | 0 | 0 | 264.2 | fast | gece2 en iyi |
| 20261007-064435 | SUBMISSION_v6c_safe@gui-timing | 82.412 | 3710.1 | 0 | 0 | 0 | 251.5 | fast | CPU boş |
| 20261007-064432 | SUBMISSION_v6c_safe@gui-timing | 82.432 | 3709.2 | 0 | 0 | 0 | 251.5 | fast | CPU boş |
| 20261007-064428 | SUBMISSION_v6c_safe@gui-timing | 82.206 | 3720.7 | 0 | 0 | 0 | 251.2 | fast | CPU boş |
| 20261007-064425 | SUBMISSION_v6c_safe@gui-timing | 82.198 | 3721.1 | 0 | 0 | 0 | 251.5 | fast | CPU boş |
| 20261007-064421 | SUBMISSION_v6c_safe@gui-timing | 81.586 | 3645.4 | 0 | 0 | 0 | 251.1 | fast | CPU boş |
| 20261007-064418 | SUBMISSION_v6c_safe@gui-timing | 81.94 | 3623.9 | 0 | 0 | 0 | 251.1 | fast | CPU boş |
| 20261007-064414 | SUBMISSION_v6c_safe@gui-timing | 82.214 | 3720.3 | 0 | 0 | 0 | 251.5 | fast | CPU boş |
| 20261007-064411 | SUBMISSION_v6c_safe@gui-timing | 82.204 | 3720.7 | 0 | 0 | 0 | 251.5 | fast | CPU boş |
| 20261007-064408 | SUBMISSION_v6c_safe@gui-timing | 81.352 | 3659.0 | 0 | 0 | 0 | 251.1 | fast | CPU boş |
| 20261007-064405 | SUBMISSION_v6c_safe@gui-timing | 82.368 | 3712.4 | 0 | 0 | 0 | 251.5 | fast | CPU boş |
| 20261007-064400 | SUBMISSION_v6c_safe | 81.352 | 3659.0 | 0 | 0 | 0 | 251.1 | fast | gece2 teslim adayı |
| 20261007-064351 | SUBMISSION_v6f_fast@gui-timing | DNF | 467.7 | 0 | 0 | 1 | 203.8 | fast | CPU boş |
| 20261007-064348 | SUBMISSION_v6f_fast@gui-timing | 80.606 | 3696.9 | 0 | 0 | 0 | 254.6 | fast | CPU boş |
| 20261007-064340 | SUBMISSION_v6f_fast@gui-timing | DNF | 468.5 | 0 | 0 | 1 | 203.7 | fast | CPU boş |
| 20261007-064333 | SUBMISSION_v6f_fast@gui-timing | DNF | 464.2 | 0 | 0 | 1 | 205.8 | fast | CPU boş |
| 20261007-064325 | SUBMISSION_v6f_fast@gui-timing | DNF | 464.3 | 0 | 0 | 1 | 205.8 | fast | CPU boş |
| 20261007-064317 | SUBMISSION_v6f_fast@gui-timing | DNF | 466.4 | 0 | 0 | 1 | 204.3 | fast | CPU boş |
| 20261007-064313 | SUBMISSION_v6f_fast@gui-timing | 79.834 | 3629.8 | 0 | 0 | 0 | 254.6 | fast | CPU boş |
| 20261007-064309 | SUBMISSION_v6f_fast@gui-timing | 80.816 | 3685.5 | 0 | 0 | 0 | 254.6 | fast | CPU boş |
| 20261007-064306 | SUBMISSION_v6f_fast@gui-timing | 79.806 | 3631.6 | 0 | 0 | 0 | 254.6 | fast | CPU boş |
| 20261007-064257 | SUBMISSION_v6f_fast@gui-timing | DNF | 468.6 | 0 | 0 | 1 | 204.0 | fast | CPU boş |
| 20261007-064252 | SUBMISSION_v6f_fast | 79.806 | 3631.6 | 0 | 0 | 0 | 254.6 | fast | gece2 teslim adayı |
| 20261007-064227 | sac_v6c_v01404 | 81.424 | 3654.8 | 0 | 0 | 0 | 251.0 | fast | gece2 finalist (TCS 5) |
| 20261007-064222 | sac_v6f_v01759 | 81.056 | 3670.7 | 0 | 0 | 0 | 247.6 | fast | gece2 finalist (TCS 5) |
| 20261007-064215 | sac_v6f_v00879 | 80.696 | 3690.8 | 0 | 0 | 0 | 249.9 | fast | gece2 finalist (TCS 5) |
| 20261007-064208 | sac_v6f_best | 79.864 | 3628.1 | 0 | 0 | 0 | 254.7 | fast | gece2 finalist (TCS 5) |
| 20261007-022954 | sac_v6b_v00249 | 81.182 | 3664.9 | 0 | 0 | 0 | 242.9 | fast | TCS 5 + safe_pos .9; S1 10/10 |
| 20261007-002521 | SUBMISSION_v4d@GUI | 81.718 | 3617.7 | 0 | 0 | 0 | 251.0 | gui |  |
| 20261007-002313 | SUBMISSION_v4d@GUI | 81.718 | 3617.7 | 0 | 0 | 0 | 251.0 | gui |  |
| 20261006-060722 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.318 | 3659.1 | 0 | 0 | 0 | 245.0 | fast | CPU boş |
| 20261006-060717 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.332 | 3658.3 | 0 | 0 | 0 | 245.1 | fast | CPU boş |
| 20261006-060712 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.696 | 3637.9 | 0 | 0 | 0 | 243.6 | fast | CPU boş |
| 20261006-060707 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.248 | 3662.7 | 0 | 0 | 0 | 245.2 | fast | CPU boş |
| 20261006-060702 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.364 | 3656.7 | 0 | 0 | 0 | 244.8 | fast | CPU boş |
| 20261006-060657 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.47 | 3650.7 | 0 | 0 | 0 | 245.1 | fast | CPU boş |
| 20261006-060653 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.398 | 3654.7 | 0 | 0 | 0 | 245.3 | fast | CPU boş |
| 20261006-060642 | sac_v4e_v00248(hızlı-riskli)@gui-timing | DNF | 1603.6 | 25 | 1 | 1 | 242.1 | fast | CPU boş |
| 20261006-060631 | sac_v4e_v00248(hızlı-riskli)@gui-timing | DNF | 1628.2 | 377 | 1 | 1 | 242.7 | fast | CPU boş |
| 20261006-060626 | sac_v4e_v00248(hızlı-riskli)@gui-timing | 81.296 | 3660.3 | 0 | 0 | 0 | 245.0 | fast | CPU boş |
| 20261006-060619 | sac_v4e_v00248(hızlı-riskli) | 80.668 | 3693.8 | 0 | 0 | 0 | 244.3 | fast | final turda 17/20 hasarsız |
| 20261006-015636 | SUBMISSION_v4d(saf-python)@gui-timing | 82.832 | 3660.1 | 0 | 0 | 0 | 249.4 | fast | numpy gizli, CPU boş |
| 20261006-015627 | SUBMISSION_v4d(saf-python)@gui-timing | 82.92 | 3654.4 | 0 | 0 | 0 | 249.6 | fast | numpy gizli, CPU boş |
| 20261006-015619 | SUBMISSION_v4d(saf-python)@gui-timing | 82.544 | 3668.6 | 0 | 0 | 0 | 244.8 | fast | numpy gizli, CPU boş |
| 20261006-015610 | SUBMISSION_v4d(saf-python)@gui-timing | 83.118 | 3648.1 | 0 | 0 | 0 | 249.1 | fast | numpy gizli, CPU boş |
| 20261006-015602 | SUBMISSION_v4d(saf-python)@gui-timing | 82.878 | 3656.3 | 0 | 0 | 0 | 249.4 | fast | numpy gizli, CPU boş |
| 20261006-015559 | SUBMISSION_v4d(numpy)@gui-timing | 82.934 | 3654.8 | 0 | 0 | 0 | 249.5 | fast | teslim dosyası, CPU boş |
| 20261006-015556 | SUBMISSION_v4d(numpy)@gui-timing | 83.064 | 3650.6 | 0 | 0 | 0 | 249.5 | fast | teslim dosyası, CPU boş |
| 20261006-015553 | SUBMISSION_v4d(numpy)@gui-timing | 82.774 | 3659.2 | 0 | 0 | 0 | 249.4 | fast | teslim dosyası, CPU boş |
| 20261006-015549 | SUBMISSION_v4d(numpy)@gui-timing | 82.296 | 3673.8 | 0 | 0 | 0 | 251.0 | fast | teslim dosyası, CPU boş |
| 20261006-015546 | SUBMISSION_v4d(numpy)@gui-timing | 82.52 | 3667.2 | 0 | 0 | 0 | 249.0 | fast | teslim dosyası, CPU boş |
| 20261006-015543 | SUBMISSION_v4d(numpy)@gui-timing | 82.886 | 3656.1 | 0 | 0 | 0 | 249.4 | fast | teslim dosyası, CPU boş |
| 20261006-015540 | SUBMISSION_v4d(numpy)@gui-timing | 82.586 | 3665.2 | 0 | 0 | 0 | 249.5 | fast | teslim dosyası, CPU boş |
| 20261006-015536 | SUBMISSION_v4d(numpy)@gui-timing | 81.736 | 3630.1 | 0 | 0 | 0 | 251.0 | fast | teslim dosyası, CPU boş |
| 20261006-015533 | SUBMISSION_v4d(numpy)@gui-timing | 82.596 | 3664.4 | 0 | 0 | 0 | 249.1 | fast | teslim dosyası, CPU boş |
| 20261006-015529 | SUBMISSION_v4d(numpy)@gui-timing | 82.454 | 3672.1 | 0 | 0 | 0 | 251.0 | fast | teslim dosyası, CPU boş |
| 20261006-015524 | SUBMISSION_v4d(numpy) | 81.736 | 3630.1 | 0 | 0 | 0 | 251.0 | fast | teslim dosyası, gömülü v4d_v02537 |
| 20261006-015457 | sac_v4d_v02537[agent_v2]@gui-timing | 82.53 | 3666.5 | 0 | 0 | 0 | 247.2 | fast | gece seçimi #1, CPU boş |
| 20261006-015452 | sac_v4d_v02537[agent_v2]@gui-timing | 82.476 | 3669.4 | 0 | 0 | 0 | 249.5 | fast | gece seçimi #1, CPU boş |
| 20261006-015448 | sac_v4d_v02537[agent_v2]@gui-timing | 82.936 | 3656.4 | 0 | 0 | 0 | 249.5 | fast | gece seçimi #1, CPU boş |
| 20261006-015442 | sac_v4d_v02537[agent_v2]@gui-timing | 82.742 | 3661.2 | 0 | 0 | 0 | 249.5 | fast | gece seçimi #1, CPU boş |
| 20261006-015437 | sac_v4d_v02537[agent_v2]@gui-timing | 82.894 | 3655.6 | 0 | 0 | 0 | 249.8 | fast | gece seçimi #1, CPU boş |
| 20261006-015432 | sac_v4d_v02537[agent_v2]@gui-timing | 82.87 | 3656.6 | 0 | 0 | 0 | 249.5 | fast | gece seçimi #1, CPU boş |
| 20261006-015427 | sac_v4d_v02537[agent_v2]@gui-timing | 82.848 | 3657.9 | 0 | 0 | 0 | 249.5 | fast | gece seçimi #1, CPU boş |
| 20261006-015421 | sac_v4d_v02537[agent_v2]@gui-timing | 82.928 | 3654.8 | 0 | 0 | 0 | 249.9 | fast | gece seçimi #1, CPU boş |
| 20261006-015416 | sac_v4d_v02537[agent_v2]@gui-timing | 82.96 | 3652.8 | 0 | 0 | 0 | 249.5 | fast | gece seçimi #1, CPU boş |
| 20261006-015411 | sac_v4d_v02537[agent_v2]@gui-timing | 82.91 | 3656.5 | 0 | 0 | 0 | 249.5 | fast | gece seçimi #1, CPU boş |
| 20261006-015404 | sac_v4d_v02537 | 81.904 | 3623.0 | 0 | 0 | 0 | 251.2 | fast | gece seçimi #1 (20/20 hasarsız) |
| 20261006-015359 | sac_v4d_v02537 | 81.904 | 3623.0 | 0 | 0 | 0 | 251.2 | fast | gece seçimi #1 (20/20 hasarsız) |
| 20261005-225342 | SUBMISSION_v2(saf-python)@gui-timing | DNF | 814.5 | 0 | 0 | 1 | 177.8 | fast | numpy gizli, eğitim yükü altında |
| 20261005-225219 | SUBMISSION_v2(saf-python)@gui-timing | DNF | 2912.5 | 0 | 0 | 1 | 202.7 | fast | numpy gizli, eğitim yükü altında |
| 20261005-225052 | SUBMISSION_v2(saf-python)@gui-timing | DNF | 3231.9 | 1 | 1 | 1 | 221.1 | fast | numpy gizli, eğitim yükü altında |
| 20261005-224931 | SUBMISSION_v2(saf-python)@gui-timing | DNF | 831.4 | 0 | 0 | 1 | 178.7 | fast | numpy gizli, eğitim yükü altında |
| 20261005-224810 | SUBMISSION_v2(saf-python)@gui-timing | DNF | 2905.4 | 0 | 0 | 1 | 193.5 | fast | numpy gizli, eğitim yükü altında |
| 20261005-224749 | SUBMISSION_v2(saf-python) | 85.704 | 3633.2 | 0 | 0 | 0 | 231.8 | fast | numpy gizli, saf Python MLP |
| 20261005-224741 | SUBMISSION_v2(numpy)@gui-timing | 87.26 | 3648.9 | 0 | 0 | 0 | 231.8 | fast | teslim dosyası, eğitim yükü altında |
| 20261005-224733 | SUBMISSION_v2(numpy)@gui-timing | 87.36 | 3645.6 | 0 | 0 | 0 | 231.7 | fast | teslim dosyası, eğitim yükü altında |
| 20261005-224726 | SUBMISSION_v2(numpy)@gui-timing | 85.704 | 3633.2 | 0 | 0 | 0 | 231.8 | fast | teslim dosyası, eğitim yükü altında |
| 20261005-224718 | SUBMISSION_v2(numpy)@gui-timing | 85.694 | 3634.1 | 0 | 0 | 0 | 232.1 | fast | teslim dosyası, eğitim yükü altında |
| 20261005-224655 | SUBMISSION_v2(numpy)@gui-timing | DNF | 1552.6 | 368 | 1 | 2 | 225.8 | fast | teslim dosyası, eğitim yükü altında |
| 20261005-224646 | SUBMISSION_v2(numpy) | 85.704 | 3633.2 | 0 | 0 | 0 | 231.8 | fast | teslim dosyası, gömülü v2_ft_v05581 |
| 20261005-155629 | sac_v2_ft_v05581[agent_v2] | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | canlı telemetri testi |
| 20261005-154841 | sac_v2_ft_v05581[agent_v2]#etrack4 | 130.356 | 7162.4 | 0 | 0 | 2 | 241.4 | fast | Corkscrew'da eğitildi, E-Track 4 hiç görmedi |
| 20261005-154834 | sac_v2_ft_v05581[agent_v2]#etrack4 | 130.356 | 7162.4 | 0 | 0 | 2 | 241.4 | fast | Corkscrew'da eğitildi, E-Track 4 hiç görmedi |
| 20261005-154517 | sac_v2_ft_v05581@GUI | 130.346 | 7066.1 | 0 | 0 | 2 | 241.4 | gui |  |
| 20261005-154146 | sac_v2_ft_v05581@GUI | 130.346 | 7066.1 | 0 | 0 | 2 | 241.4 | gui |  |
| 20261005-153440 | sac_v2_ft_v05581[agent_v2]@gui-timing | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153434 | sac_v2_ft_v05581[agent_v2]@gui-timing | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153430 | sac_v2_ft_v05581[agent_v2]@gui-timing | 97.132 | 3649.7 | 0 | 0 | 0 | 202.8 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153424 | sac_v2_ft_v05581[agent_v2]@gui-timing | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153419 | sac_v2_ft_v05581[agent_v2]@gui-timing | 96.82 | 3657.1 | 0 | 0 | 0 | 202.0 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153413 | sac_v2_ft_v05581[agent_v2]@gui-timing | 160.832 | 3659.8 | 24 | 1 | 1 | 202.8 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153407 | sac_v2_ft_v05581[agent_v2]@gui-timing | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153400 | sac_v2_ft_v05581[agent_v2]@gui-timing | 87.392 | 3641.5 | 0 | 0 | 0 | 231.0 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153354 | sac_v2_ft_v05581[agent_v2]@gui-timing | 96.16 | 3675.6 | 0 | 0 | 0 | 203.0 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153350 | sac_v2_ft_v05581[agent_v2]@gui-timing | 95.386 | 3642.3 | 0 | 0 | 1 | 203.7 | fast | agent v2: ısınma + kuyruk boşaltma |
| 20261005-153247 | sac_v2_ft_v05581@gui-timing | 88.818 | 3658.7 | 0 | 0 | 0 | 231.0 | fast | v2 seçim #1 |
| 20261005-153235 | sac_v2_ft_v05581@gui-timing | DNF | 1535.5 | 1 | 1 | 2 | 202.8 | fast | v2 seçim #1 |
| 20261005-153224 | sac_v2_ft_v05581@gui-timing | DNF | 1527.7 | 305 | 2 | 1 | 202.8 | fast | v2 seçim #1 |
| 20261005-153214 | sac_v2_ft_v05581@gui-timing | DNF | 976.7 | 186 | 1 | 1 | 173.0 | fast | v2 seçim #1 |
| 20261005-153202 | sac_v2_ft_v05581@gui-timing | DNF | 944.6 | 411 | 1 | 1 | 202.8 | fast | v2 seçim #1 |
| 20261005-153157 | sac_v2_ft_v05581@gui-timing | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | v2 seçim #1 |
| 20261005-153146 | sac_v2_ft_v05581@gui-timing | DNF | 979.0 | 308 | 1 | 1 | 178.6 | fast | v2 seçim #1 |
| 20261005-153135 | sac_v2_ft_v05581@gui-timing | DNF | 1062.4 | 0 | 0 | 0 | 202.8 | fast | v2 seçim #1 |
| 20261005-153125 | sac_v2_ft_v05581@gui-timing | DNF | 3316.5 | 0 | 0 | 1 | 203.7 | fast | v2 seçim #1 |
| 20261005-153114 | sac_v2_ft_v05581@gui-timing | DNF | 1869.0 | 39 | 1 | 1 | 201.2 | fast | v2 seçim #1 |
| 20261005-153107 | sac_v2_ft_v05581 | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | v2 seçim #1 (10/10 hasarsız) |
| 20261005-153101 | sac_v2_ft_v05581 | 85.736 | 3630.9 | 0 | 0 | 0 | 231.0 | fast | v2 seçim #1 (10/10 hasarsız) |
| 20261005-151924 | snakeoil3_gym#etrack4@GUI | 113.684 | 7065.6 | 1585 | 7 | 5 | 302.3 | gui |  |
| 20261005-151545 | snakeoil3_gym#etrack4@GUI | 113.684 | 7065.6 | 1585 | 7 | 5 | 302.3 | gui |  |
| 20261005-131145 | sac_g995_best@gui-timing | 95.276 | 3641.2 | 0 | 0 | 0 | 249.1 | fast | g995 best.pt (60. dk) |
| 20261005-131135 | sac_g995_best@gui-timing | 87.612 | 3635.4 | 0 | 0 | 0 | 249.1 | fast | g995 best.pt (60. dk) |
| 20261005-131108 | sac_g995_best@gui-timing | DNF | 1520.8 | 0 | 0 | 1 | 225.8 | fast | g995 best.pt (60. dk) |
| 20261005-131041 | sac_g995_best@gui-timing | DNF | 1118.2 | 107 | 1 | 1 | 225.8 | fast | g995 best.pt (60. dk) |
| 20261005-131021 | sac_g995_best@gui-timing | DNF | 1599.3 | 24 | 1 | 1 | 225.8 | fast | g995 best.pt (60. dk) |
| 20261005-131002 | sac_g995_best@gui-timing | DNF | 1365.3 | 233 | 1 | 2 | 192.9 | fast | g995 best.pt (60. dk) |
| 20261005-130934 | sac_g995_best@gui-timing | DNF | 1710.9 | 0 | 0 | 2 | 223.2 | fast | g995 best.pt (60. dk) |
| 20261005-130916 | sac_g995_best@gui-timing | DNF | 3554.0 | 4 | 1 | 1 | 202.7 | fast | g995 best.pt (60. dk) |
| 20261005-130901 | sac_g995_best@gui-timing | DNF | 956.8 | 0 | 0 | 1 | 225.8 | fast | g995 best.pt (60. dk) |
| 20261005-130846 | sac_g995_best@gui-timing | DNF | 1194.4 | 0 | 0 | 2 | 181.6 | fast | g995 best.pt (60. dk) |
| 20261005-130837 | sac_g995_best | 87.612 | 3635.4 | 0 | 0 | 0 | 249.1 | fast | g995 best.pt (60. dk), seçimde 5/10 hasarsız |
| 20261005-130829 | sac_g995_best | 87.612 | 3635.4 | 0 | 0 | 0 | 249.1 | fast | g995 best.pt (60. dk), seçimde 5/10 hasarsız |
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
