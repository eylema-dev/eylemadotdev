# Eyleme web sitesi

Güncel ürün adı **Eyleme**. GitHub organizasyonu artık **eyleme-dev**; mevcut `eylema.dev` alan adı ve varlık adresleri korunur. [Ad uyarlama kaydına](records/project-name-alignment.tr.md) bakın.

Hedef alan adı `eylema.dev` olan iki dilli tanıtım sitesinin herkese açık kaynak deposu: [eyleme-dev/eylemadotdev](https://github.com/eyleme-dev/eylemadotdev).

Açık platform projesi: [eyleme-dev/eyleme](https://github.com/eyleme-dev/eyleme). Bu depo uygulanmış yerel görev temelini ve önerilen işbirlikçi döngü platformunu tanıtır; Rust platformunu içermez veya çalıştırmaz.

[English](README.md)

Arama ilkesi: bakım sorumlusu Google ve Bing sonuçlarından kaldırma istedi. Site artık sayfa ve kaynak yanıtlarında noindex gerektirir, tarama erişimini korur ve IndexNow gönderimini kapatır. Yayın, geçici kaldırma istekleri ve nihai indeks durumu ayrıdır; [arama görünürlüğüne](docs/tr/discovery.md) bakın.

## Web sitesi

Varsayılan İngilizce `/`, Türkçe `/tr/` adresindedir. İkisi de karşılıklı hreflang ve kendi canonical adresine sahip tam HTML belgeleridir. Mimari sekmeleri HTML'de zaten bulunan içeriği kademeli olarak geliştirir. Sorular doğal açılır/kapanır kontroller kullanır. Hesap, analitik, çerez, uzak yazı tipi, model API'si veya üçüncü taraf çalışma zamanı paketi yoktur.

Yerel önizleme:

```sh
python3 -m venv .venv
.venv/bin/python tools/build.py
.venv/bin/python -m http.server 4187 --bind 127.0.0.1 --directory public
```

`http://127.0.0.1:4187/` adresini açın. Statik yayın dizini `public/` klasörüdür; Python yalnızca geliştirme/CI aracıdır. Deponun kökünü veya geliştirme sunucusunu üretim ortamında yayınlamayın.

## Kaynaklar ve kontroller

- [Katkı akışı](CONTRIBUTING.tr.md), [kalite kontrolleri](docs/tr/quality-gates.md), [araçlar ve varlıklar](docs/tr/tooling.md).
- [SEO, üretken arama ve yayına hazırlık](docs/tr/discovery.md).
- [Görev planı](records/plan.tr.md), [tasarım tanımı](records/design.tr.md) ve [doğrulama](records/verification.tr.md).
- `content/*.json`: incelenen iki dilli metin; `tools/build.py`: belirlenimci HTML, JSON-LD, robots, sitemap ve 404 üretimi; `public/assets/`: özgün CSS/JS ve marka görselleri.

[AGENTS.md](AGENTS.md) içindeki doğrulama komutlarını aynen çalıştırın. Üretilen belgeler sürüm kontrolündedir; CI güncelliğini denetler. Çeviri özetleri inceleme kaydıdır, anlam eşdeğerliğinin kanıtı değildir. Site kontrolleri çekirdek, GPU, model, eğitim veya tam ürün kabulünü kanıtlamaz. [Güncel platform hizalaması](records/platform-v07-alignment.tr.md) [sabitlenmiş kaynak kaydına](records/platform-source-snapshot.json) dayanır; [v0.7 iki dilli görseli](records/architecture-v07-visuals.tr.md) artık aynı platform, proje bilgisi/belleği ve planlanan yerel iyileştirmeyi gösterir; sınırlı bileşen kabulü ayrı kalır. [Yerleşik üretim istemleri](records/architecture-v07-prompts.json) ve varlık özetleri kaydedilmiştir.

## Yayınlama sınırı

Kaynak deposu, proje sahibinin açık isteğiyle herkese açıktır. Yayınlanan HTML, CSS, JavaScript ve görseller herkes tarafından alınabilir. Yetkili üretim hedefi `umayos subscription`, West Europe, `rg-eylema-dev / swa-eylema-dev` altında Azure Static Web Apps Free katmanıdır. Üretim iş akışı yalnızca `public/` çıktısını doğrular ve yükler; canlı dosya özetlerini, MIME türlerini, yönlendirmeyi ve `/release.json` commit değerini kontrol eder. [Yayın sözleşmesini](records/deployment.tr.md) ve hazırlık listesini izleyin. Search Console/Bing doğrulaması, indeksleme ve saha performansı ayrı kanıtlardır. Yerel kontroller tek başına dağıtımı doğrulamaz.
