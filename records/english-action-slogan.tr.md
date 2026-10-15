# İngilizce eylem sloganı

[English](english-action-slogan.md). Görev WEB-024, sürüm 0.1.0, 15 Ekim 2026.

## İstek ve plan

Yetki: bakım sorumlusu İngilizce sloganın “Durma Eyleme Geç” ile aynı mesajı veren “Don’t stop. Take action.” olmasını doğrudan istedi; kontrollerin tamamlanmasına ve sitenin yayımlanmasına izin verdi. Taban: güncel `origin/main` olan `871b9dd6730cc7335f82a49a18dc339c283039da`. Dal: mevcut yalıtılmış site çalışma ağacındaki `codex/english-action-slogan`.

İzinli yollar: `content/en.json`, üretilen `public/index.html`, bu iki dilli kayıt ve `tools/translation-pairs.json`. Plan: mevcut üç satırlı düzende İngilizce başlığı güncellemek, anlamını Türkçeyle karşılaştırmak, sayfayı ve çeviri parmak izlerini yeniden üretmek, depo kontrollerini çalıştırmak, masaüstü/mobil görünümü doğrulamak, farkı öz incelemeden geçirmek, PR üzerinden teslim etmek ve yayımlanan birleştirme sürümünü doğrulamak.

## Kabul, risk ve bütçeler

- Tam sloganlar: İngilizce ve Türkçe oluşturulan başlıkları, boşlukları normalleştirerek incelemek.
- Duyarlı görünüm: masaüstü ve mobil ekran görüntülerini, 320 pikselde taşmayı, yüklenen üçgenleri ve dil geçişini incelemek.
- Yerel kapılar: katkıcı komutlarının tamamı, belirlenimci üretim kontrolü, çeviri incelemesi, doldurulmuş PR gövdesi doğrulaması ve boşluk kontrolü.
- Yayın: PR'nin tam sürümündeki kontroller ve inceleme konuları, birleştirme sonrası main kontrolleri, Azure dağıtım durumu, kanonik HTTPS sürüm kimliği ve dosya özetleri, ardından canlı tarayıcı doğrulaması.

Bütçe: 30 dakika ve başarısız kapı başına en çok üç odaklı onarım; yeni bağımlılık veya ücretli kaynak yok. Risk: başlığın satıra sığmaması veya üretilen sayfanın eski kalması. Geri dönüş: bu sınırlı metin değişikliğini geri alıp yeniden yayımlamak. Türkçe başlık ve ortak üçgen güncelliğini korur; iki slogan aynı eyleme geçme çağrısını ifade eder.

## Roller ve kanıt

Mimar, uygulayıcı, doğrulayıcı ve öz inceleyici: Python, Git/GitHub CLI, Azure CLI ve mevcut paketli Playwright/Chromium kullanan bu Codex GPT-6 oturumu. Ayrı bir inceleyici iddiası yoktur. Kontrol sonuçları PR ve teslim raporuna kaydedilir; bu plan tek başına kontrollerin geçtiğini veya yayını kanıtlamaz. Ürün çalışma zamanı, saha kurulumu ve ticari hizmet kabulü bu metin değişikliğine uygulanmaz.
