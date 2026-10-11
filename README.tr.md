# Eylema web sitesi

Hedef alan adı `eylema.dev` olan iki dilli tanıtım sitesinin herkese açık kaynak deposu: [eylema-dev/eylemadotdev](https://github.com/eylema-dev/eylemadotdev).

Açık proje tasarımı: [eylema-dev/eylema](https://github.com/eylema-dev/eylema). Bu depo planlanan Rust platformundan ayrıdır. Deponun oluşturulması sitenin yayınlandığını göstermez.

[English](README.md)

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

[AGENTS.md](AGENTS.md) içindeki doğrulama komutlarını aynen çalıştırın. Üretilen belgeler sürüm kontrolündedir; CI güncelliğini denetler. Çeviri özetleri inceleme kaydıdır, anlam eşdeğerliğinin kanıtı değildir. Site, Eylema'nın planlanan Rust, GPU veya model çalışma zamanını uygulamaz veya göstermez.

## Yayınlama sınırı

Kaynak deposu, proje sahibinin açık isteğiyle herkese açıktır. Yayınlanan HTML, CSS, JavaScript ve görseller herkes tarafından alınabilir. Barındırma, DNS, Search Console/Bing doğrulaması ve canlı indeksleme bu kodla kurulmaz. Yayınlamadan önce hazırlık listesini izleyin. Yerel kontroller dağıtım veya uygulama performansı iddiasını doğrulamaz.
