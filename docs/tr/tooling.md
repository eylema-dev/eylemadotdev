# Site araçları ve varlık kökeni

[English](../en/tooling.md).

| Sınır | Envanter |
|---|---|
| Yayınlanan çalışma zamanı | Tarayıcı HTML/CSS ve 1.7 KB birinci taraf JavaScript; paket indirme, uzak font, analitik veya çıkarım motoru yok |
| Derleme ve CI | Python 3.14 standart kütüphanesi; boş bağımlılık listesi kasıtlı; yalnızca geliştirme |
| CI eylemleri | checkout v7.0.1: `3d3c42e5aac5ba805825da76410c181273ba90b1`; setup-python v7.0.0: `5fda3b95a4ea91299a34e894583c3862153e4b97`; resmi etiket SHA'ları 11 Ekim 2026'da kontrol edildi |
| Yerel görsel üretim | Codex ve yerleşik Image Gen; dört bölüm konsepti ve bir ayrı varlık; site API anahtarı yok |
| Varlık kodlama | Paketli sharp 0.35.5, yalnızca geliştirme; 1024px ve 640px WebP, kalite 88; HTML üretmek/sunmak için gerekmez |
| Tarayıcı doğrulaması | CUA üzerinden Codex uygulama içi tarayıcısı; IAB içinde bulunmayan JavaScript kapatma ve azaltılmış hareket seçenekleri için ek paketli Playwright Chromium 151.0.7922.34; yalnızca geliştirme |
| Ana platform | Tarayıcı/işletim sistemi görsel işlemesi ve sistem Helvetica Neue/Helvetica/Arial; yalnızca Rust yığını iddiası değil |

`public/assets/eylema.svg`, `favicon.svg`, `apple-touch-icon.png` ve `social.png`, 11 Ekim 2026'da kaynak çalışma alanında bulunan, proje sahibinin Eylema marka paketinin değiştirilmemiş kopyalarıdır. Düzenlenebilir vektör kaynakları platform çalışma alanındadır. Üçüncü taraf font dosyası veya stok görsel dağıtılmaz. Varlık özetleri [asset-provenance.json](../../records/asset-provenance.json) içindedir.

Şerit heykeli, özgün üretilmiş temsili görseldir. İstemi ve amacı [tasarım kaydındadır](../../records/design.tr.md). Seçilen ayrı görsel `eylema-loop-1024.webp` (47.100 bayt) ve `eylema-loop-640.webp` (20.088 bayt) olarak kodlandı. Görsel bir benzetmedir; uygulanmış GPU sahnesi veya ürün ekran görüntüsü değildir.

PR açıklama denetleyicisi ve şablonu, proje sahibinin bekleyen Eylema katkı altyapısından kopyalandı; birinci taraf depo araçlarıdır. Bu site, platform için dağıtım lisansı seçmez veya marka lisansı vermez.
