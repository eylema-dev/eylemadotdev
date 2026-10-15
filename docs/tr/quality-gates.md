# Web sitesi kalite kontrolleri

[English](../en/quality-gates.md).

Web sitesi, platform belgeleri deposundan ayrıdır. Standart kütüphane doğrulayıcısı, uygulama şeması veya Rust çalışma zamanı testlerini taşımak yerine site sınırını kontrol eder. Platformun kontrolleri bu depoyla değiştirilmez.

| Kontrol | Kanıt ve sınırlar |
|---|---|
| Üretilen çıktı | HTML, sitemap, robots ve 404; üretici ve iki dilli metinle eşleşir |
| Keşfedilebilirlik | Tek H1/main, dil, kendi canonical adresi, karşılıklı hreflang/x-default, açıklama, tek index,follow ilkesi, JSON-LD tutarlılığı, yerel varlık/çapalar, taramaya izin veren robots ve tam iki dilli sitemap, görünür güncel temel kapsamı ve mimari görseli kapsam bildirimi |
| Çeviri | Anahtar/dizi yapısı ve adım tanımlayıcıları eşleşir; incelenen SHA-256 özetleri günceldir; anlam incelemesi ayrıdır |
| Regresyon testleri | Eksik çeviri/varlık, tanımlayıcı kayması, yanlış canonical/hreflang, yeniden eklenen noindex veya çelişkili yönergeler, tekrarlanan ID, yapılandırılmış iddia kayması, eski özet ve HTML/script enjeksiyonu reddedilir |
| Statik bütçe | CSS/JS toplamı sıkıştırılmamış 35 KB altında; bu boyut bütçesidir, Core Web Vitals ölçümü değildir |
| PR açıklaması | Gerekli bölümler somut değer içerir; doğruluk ve yetki inceleme gerektirir |
| Tarayıcı | Gerçek gezinme, diller, sekmeler/klavye, açılır yanıtlar, mobil düzen, konsol ve görsel karşılaştırma ayrı kontrol edilir |
| Yayın | Kısa/yanlış commit, eksik çıktı, sembolik bağlantı ve değişmiş canlı envanter reddedilir; sunucu kontrolü SPA fallback, sahte 404, varlık yönlendirmesi ve genel/rotaya özel indeksleme kurallarını reddeder; canlı kontroller kaynaklarda ve normalleştirilmiş giriş sayfalarında engelleyici başlıkları reddeder; üretim akışı kapsamlı anahtarı yalnızca doğrulama sonrası kullanır |
| CI | Salt okunur PR akışı, sabitlenmiş eylemler; PR kontrollerinde gizli anahtar/dağıtım yok; PR başı ve kontrol edilen SHA yazdırılır |

[AGENTS.md](../../AGENTS.md) komutlarını ve `python tools/build.py --check` komutunu sanal ortamda çalıştırın. `--allow-template` yalnızca boş PR formunu denetler. Yeşil CI bağımsız veya proje sahibi incelemesi değildir. Depo, dal korumasını yapılandırmaz.

Barındırma, HTTPS/yönlendirmeler, gerçek HTTP 404, indeksleme, saha performansı, model/GPU/Rust yürütmesi ve uluslararası erişim ayrı kanıt gerektirir. Eksik donanım kanıtı site kontrollerinden çıkarılamaz.

IndexNow varsayılan olarak ağsız önizler; açık gönderim sunucu/anahtar/sayfa ön kontrolünü geçer, yönlendirme/tekrar olmadan tek POST yollar ve gerçek200/202/hata alındısını korur. Yeni alanın indekslenebilir yayını, sahip panosu gönderim kabulü ve gözlenen indeksleme durumu ayrı kanıtlardır. Eski alanın kaldırma kanıtı tarihseldir. Canonical DNS hatası başarısız canlı kapı olarak kalır. [Arama görünürlüğüne](discovery.md) bakın.
