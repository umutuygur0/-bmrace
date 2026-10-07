# Teslim gereksinimleri ve teslim planı (henüz uygulanmadı)

Kaynak: organizatör yönlendirmesi (2026-10-07'de kullanıcı paylaştı) + Session 1 sunumu. Teslim: **11 Ekim Pazar**.

## Organizatörün istediği paket
**🎥 Video:** standing start fastest lap
- tur **Corkscrew** pistinde olmalı
- **duran kalkıştan** olmalı
- resmi teslim için **livery değiştirilmemeli** (video varsayılan boyayla)

**💻 GitHub reposu:** AI araç kodu + araç livery'si
- repo **herkese açık** olmalı
- **araç modelinin dinamikleri değiştirilmemeli** (biz değiştirmedik: car1-ow1.xml dokunulmadı;
  vites/ABS/patinaj kuralları sürücü kodunun parçası)
- livery **"mass start show"** (çok araçlı toplu kalkış gösterisi) için kullanılacak

## Durum (2026-10-07)
- Teslim agent'ı: `racelab/submission/torcs_jm_par_rl.py` (model `rl/snapshots/v4d_v02537_best.pt`)
- **Gerçek GUI'de doğrulandı: Corkscrew 01:21:73 (81,73 s), hasar 0, max 251 km/h** (2 koşu, ikisi aynı)
- Livery: yapılmadı. Kullanıcı kararı: puan getirmiyorsa **basit** bir şey yeterli.

## ⚠️ Repo uyarısı
Mevcut proje reposu herkese açık yapılmamalı. İçinde şunlar var:
- `AI-Racing-Session-1 - Updated.pdf` → son sayfa: "Submitted for evaluation purpose only as per existing NDA"
- IBM kurulum rehberleri (docx), RaceRunner kurulum dosyası, TORCS kurulumu (1,2 GB), başkalarının repoları (ıncelenen_repos)
→ Öneri: proje dışında **ayrı temiz repo** (sadece kendi kodumuz, model, livery, README, lap log).

## Teslim aşamasında yapılacaklar (kullanıcı "teslime geçelim" deyince)
1. Video rehberi: Win+Alt+R (Xbox Game Bar) ile TORCS kaydı; Corkscrew, yalnız scr_server 1, 1 tur, varsayılan livery.
2. Temiz repo klasörü + README (nasıl çalıştırılır, yaklaşım, sonuçlar) — push kullanıcı onayıyla.
3. Basit livery: `drivers/scr_server/0/car1-ow1.rgb` kopyasından renk değişikliği (PIL), sadece repoya; TORCS'a yüklenmez.
4. (Önerilir) Mass start testi: birden çok araçla Corkscrew'da çarpışma riskini ölç (model rakipleri görmüyor).
