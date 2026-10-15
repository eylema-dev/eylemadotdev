# Site araçları ve varlık kökeni

[English](../en/tooling.md).

| Sınır | Envanter |
|---|---|
| Yayınlanan çalışma zamanı | Tarayıcı HTML/CSS ve 1.7 KB birinci taraf JavaScript; paket indirme, uzak font, analitik veya çıkarım motoru yok |
| Derleme ve CI | Python 3.14 standart kütüphanesi; boş bağımlılık listesi kasıtlı; yalnızca geliştirme |
| CI eylemleri | checkout v7.0.1: `3d3c42e5aac5ba805825da76410c181273ba90b1`; setup-python v7.0.0: `5fda3b95a4ea91299a34e894583c3862153e4b97`; resmi etiket SHA'ları 11 Ekim 2026'da kontrol edildi; üretim akışı için Azure/static-web-apps-deploy v1 `4d27395796ac319302594769cfe812bd207490b1` resmi deposundan doğrulandı |
| Yerel görsel üretim | Codex ve yerleşik Image Gen; dört bölüm konsepti ve bir ayrı varlık; site API anahtarı yok |
| Varlık kodlama | Paketli sharp 0.35.5, yalnızca geliştirme; 1024px ve 640px WebP, kalite 88; HTML üretmek/sunmak için gerekmez |
| Tarayıcı doğrulaması | CUA üzerinden Codex uygulama içi tarayıcısı; IAB içinde bulunmayan JavaScript kapatma ve azaltılmış hareket seçenekleri için ek paketli Playwright Chromium 151.0.7922.34; yalnızca geliştirme |
| Ana platform | Tarayıcı/işletim sistemi görsel işlemesi ve sistem Helvetica Neue/Helvetica/Arial; yalnızca Rust yığını iddiası değil |

`public/assets/eylema.svg`, `favicon.svg`, `apple-touch-icon.png` ve `social.png`, 11 Ekim 2026'da kaynak çalışma alanında bulunan, ilk olarak proje sahibinin o tarihteki Eylema marka paketinden kopyalandı. Düzenlenebilir vektör kaynakları platform çalışma alanındadır. Üçüncü taraf font dosyası veya stok görsel dağıtılmaz. Varlık özetleri [asset-provenance.json](../../records/asset-provenance.json) içindedir.

Şerit heykeli, özgün üretilmiş temsili görseldir. İstemi ve amacı [tasarım kaydındadır](../../records/design.tr.md). Seçilen ayrı görsel `eylema-loop-1024.webp` (47.100 bayt) ve `eylema-loop-640.webp` (20.088 bayt) olarak kodlandı. Görsel bir benzetmedir; uygulanmış GPU sahnesi veya ürün ekran görüntüsü değildir.

[Teknoloji görseli güncellemesi](../../records/technology-visual.tr.md), proje sahibinin onayladığı İngilizce posteri ve Türkçe eşini ekler; ikisi de 1672 × 941 boyutundadır. Özgün PNG'ler tam boy sunulur; kayıpsız WebP kopyaları sayfa içi önizlemeleri sağlar. Yerleşik Image Gen, Türkçe başlığı onaylı İngilizce EylemA yazısıyla eşleştirmiş ve aynı referanstan şeffaf marka görselini çıkarmıştır. Sharp 0.35.5 marka görselini alfa kanalını koruyarak 960 × 320 boyutuna getirmiştir. İlk E, turuncu E simgesidir; ardından `ylemA` gelir. Yeni üst/alt başlık görseli ek font veya tarayıcı paketi yüklemez. Özgün marka paketi varlıkları erişilebilir kalır.

PR açıklama denetleyicisi ve şablonu, proje sahibinin bekleyen Eylema katkı altyapısından kopyalandı; birinci taraf depo araçlarıdır. Bu site, platform için dağıtım lisansı seçmez veya marka lisansı vermez.

[v0.5 görsel değişimi](../../records/architecture-v05-visuals.tr.md), üç yerleşik Image Gen çağrısı kullanır: İngilizce yeniden tasarım, belirli ok bağlantılarının düzeltmesi ve Türkçe yerelleştirme. İki yeni kaynak 1672 × 941 PNG; kayıpsız WebP önizlemeleri aynı paketli sharp 0.35.5 ile kodlanır. Mevcut görsel adresleri bakımcının açık talebiyle değiştirilir; başlık yazı işareti, ana görsel ve diğer marka varlıkları korunur. [İstem kümesi](../../records/architecture-v05-prompts.json) kesin metinleri ve ok kısıtlarını kaydeder. Önerilen entegrasyon ile ayrı uygulanmış görev temeli görselde ve HTML’de görünür.

[v0.7 poster değişimi](../../records/architecture-v07-visuals.tr.md) dört yerleşik Image Gen çağrısı kullanır: İngilizce yeniden tasarım, iki dar ok düzeltmesi ve Türkçe yerelleştirme. İki PNG yine 1672 × 941; kayıpsız sharp 0.35.5 WebP önizlemeleri var. [Tam istem kümesi](../../records/architecture-v07-prompts.json), özet ve bayt boyutları kaydedildi. Mevcut poster adresleri açık taleple değiştirildi; diğer varlıklar korunur. Entegre tasarım, kaynak kapıları ve planlanan yerel eğitim, sınırlı temel kanıtından ayrıdır.

[Ürün adı güncellemesi](../../records/project-name-alignment.tr.md) etkin markayı **Eyleme** olarak değiştirir. Düzenlenebilir vektör paketi sözcük işaretini, sosyal kartı ve logo PNG dosyalarını yeniden üretti; simge değişmedi. Üç yerleşik Image Gen çağrısı saydam başlık logosunda ve İngilizce/Türkçe v0.7 afişlerinde eski son A harfini dar kapsamda e ile değiştirdi. Mevcut varlık yolları ve gerçek eylema.dev alan adı korundu. Yukarıdaki önceki üretim kayıtları tarihsel revizyonlarını açıklar. Güncel özetler varlık köken envanterindedir.

## Güncel Eyleme varlıkları — 15 Ekim 2026

[Site kimliği geçişi](../../records/website-identity.tr.md) güncel dosyaları `eyleme-*` olarak adlandırır ve eyleme.dev adresini hazırlar. Logo zaten Eyleme yazar; İngilizce/Türkçe mimari afişlerinde yalnızca alt bilgi alan adı değişir. Yukarıdaki önceki üretim notları tarihseldir. Köken envanteri güncel dosya adlarını, baytları ve özetleri kaydeder.
