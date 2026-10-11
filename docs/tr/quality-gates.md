# Web sitesi kalite kontrolleri

[English](../en/quality-gates.md).

Web sitesi, platform belgeleri deposundan ayrıdır. Standart kütüphane doğrulayıcısı, uygulama şeması veya Rust çalışma zamanı testlerini taşımak yerine site sınırını kontrol eder. Platformun kontrolleri bu depoyla değiştirilmez.

| Kontrol | Kanıt ve sınırlar |
|---|---|
| Üretilen çıktı | HTML, sitemap, robots ve 404; üretici ve iki dilli metinle eşleşir |
| Keşfedilebilirlik | Tek H1/main, dil, kendi canonical adresi, karşılıklı hreflang/x-default, açıklama, indekslenebilirlik, JSON-LD tutarlılığı, yerel varlık/çapalar ve sitemap adresleri |
| Çeviri | Anahtar/dizi yapısı ve adım tanımlayıcıları eşleşir; incelenen SHA-256 özetleri günceldir; anlam incelemesi ayrıdır |
| Regresyon testleri | Eksik çeviri/varlık, tanımlayıcı kayması, yanlış canonical/hreflang, noindex, tekrarlanan ID, yapılandırılmış iddia kayması, eski özet ve HTML/script enjeksiyonu reddedilir |
| Statik bütçe | CSS/JS toplamı sıkıştırılmamış 35 KB altında; bu boyut bütçesidir, Core Web Vitals ölçümü değildir |
| PR açıklaması | Gerekli bölümler somut değer içerir; doğruluk ve yetki inceleme gerektirir |
| Tarayıcı | Gerçek gezinme, diller, sekmeler/klavye, açılır yanıtlar, mobil düzen, konsol ve görsel karşılaştırma ayrı kontrol edilir |
| CI | Salt okunur GitHub çalıştırıcısı, sabitlenmiş eylemler; gizli anahtar ve dağıtım yok; PR başı ve kontrol edilen SHA yazdırılır |

[AGENTS.md](../../AGENTS.md) komutlarını ve `python tools/build.py --check` komutunu sanal ortamda çalıştırın. `--allow-template` yalnızca boş PR formunu denetler. Yeşil CI bağımsız veya proje sahibi incelemesi değildir. Depo, dal korumasını yapılandırmaz.

Barındırma, HTTPS/yönlendirmeler, gerçek HTTP 404, indeksleme, saha performansı, model/GPU/Rust yürütmesi ve uluslararası erişim ayrı kanıt gerektirir. Eksik donanım kanıtı site kontrollerinden çıkarılamaz.
