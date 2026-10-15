# Eyleme web sitesi

Ürün ve site kimliği **Eyleme**. Depo **eyleme-dev/eylemedotdev**, hazırlanan canonical alan adı **eyleme.dev**. Proje sahibi eylema.dev adresini kapattı ve artık eyleme.dev adresini GoDaddy’den aldı. [Özel alan adı açılışı](records/eyleme-domain.tr.md) mevcut Azure Free sitesini yeni adrese bağlar; DNS, Azure doğrulaması ve normal HTTPS ayrı kabul eşikleridir. [Site kimliği kaydına](records/website-identity.tr.md) bakın.

Hedef alan adı `eyleme.dev` olan iki dilli tanıtım sitesinin herkese açık kaynak deposu: [eyleme-dev/eylemedotdev](https://github.com/eyleme-dev/eylemedotdev).

Herkese açık açık kaynak proje: [eyleme-dev/eyleme](https://github.com/eyleme-dev/eyleme). **Eyleme**, hem ortak marka hem de bağımsız kullanılabilen topluluk aracıdır. Birinci taraf çekirdek kod ve belgeler Apache-2.0 lisanslıdır; üçüncü taraf/model/veri koşulları ve site varlıkları kendi sınırlarını korur. **Eyleme Derleme** ve **Eyleme Onama**, kapalı kaynak ve ücretli abonelik modeliyle geliştirilen ürünlerdir. Herkese açık tanımları [eyleme.dev/tr/#products](https://eyleme.dev/tr/#products) adresinde yer alır; private kaynak bağlantısı, uydurma fiyat veya etkin ödeme akışı içermez. [Tek marka ürün kaydına](records/single-brand-family.tr.md) bakın.

Bu depo uygulanmış yerel görev temelini ve önerilen işbirlikçi döngü platformunu tanıtır; Rust platformunu içermez veya çalıştırmaz. Ticari ürünler isteğe bağlıdır: Eyleme yerel izin kontrollerini korur ve bu abonelikler olmadan çalışır. Ailenin sunum sırası Derleme → Onama → Eyleme’dir; politika denetimi aşamalar arasında da uygulanır.

[English](README.md)

Arama ilkesi: proje sahibi 15 Ekim 2026 tarihinde yeni eyleme.dev alan adının Google/Bing keşfini açıkça yetkilendirdi. Canonical giriş sayfaları indekslenebilir, sitemap İngilizce ve Türkçeyi içerir, gerçek404 noindex kalır. Eski eylema.dev kaldırma takibi ayrıdır. Motor doğrulaması/gönderimi ve gerçek indekslenme farklıdır; [arama görünürlüğüne](docs/tr/discovery.md) ve [WEB-020](records/search-launch.tr.md) kaydına bakın.

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

Yetkili yayın hedefi [eyleme.dev](https://eyleme.dev/) adresidir. Dağıtım iş akışı canonical sunucuda tam yayın SHA, özet, MIME, indekslenebilir yanıtlar, yönlendirme ve gerçek 404 değerlerini doğrular. İki sertifika geçerli olduktan sonra www ve Azure adresi yolu koruyarak kök alan adına yönlenir. Güncel kabul kanıtı için [WEB-018](records/eyleme-domain.tr.md) kaydına bakın. Alan adı satın almayı ya da indekslemeyi geri açmayı örtük olarak uygulamayın.

Kaynak deposu, proje sahibinin açık isteğiyle herkese açıktır. Yayınlanan HTML, CSS, JavaScript ve görseller herkes tarafından alınabilir. Yetkili üretim hedefi `umayos subscription`, West Europe, `rg-eylema-dev / swa-eylema-dev` altında Azure Static Web Apps Free katmanıdır. Üretim iş akışı yalnızca `public/` çıktısını doğrular ve yükler; canlı dosya özetlerini, MIME türlerini, yönlendirmeyi ve `/release.json` commit değerini kontrol eder. [Yayın sözleşmesini](records/deployment.tr.md) ve hazırlık listesini izleyin. Search Console/Bing doğrulaması, indeksleme ve saha performansı ayrı kanıtlardır. Yerel kontroller tek başına dağıtımı doğrulamaz.
