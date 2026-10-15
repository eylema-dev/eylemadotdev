# Ekosistem, saha verisi ve uzmanlık abonelikleri

[English](ecosystem-positioning.md). Görev WEB-023, revizyon 0.1.0, 15 Ekim 2026.

## İstek ve plan

Yetki: bakım sorumlusunun bu sohbette siteyi Eyleme'nin açık kaynak topluluk ekosistemi, Derleme'nin fiziksel dünyadan veri toplama ve bulut/kurum içi kayıt kapsamı, Onama'nın siber güvenlik, yetki, sorumluluk ve mevzuat süreçleri doğrultusunda güncelleme isteği. Derleme ve Onama ücretli uzmanlık ürünleridir. İstek, site revizyonuna ve taslak PR'a yetki verir; yayına, faturalamaya, depo görünürlüğü veya izin değişikliğine yetki vermez.

Taban: site deposunun güncel `origin/main` sürümü `b3b5e14382be7e87bf6ade2aa027e9c5db55c256`. Dal: `codex/website-ecosystem-positioning`. Ayrı çalışma ağacı diğer çalışma kopyalarını korur. İzinli yollar: `content/en.json`, `content/tr.json`, `tools/build.py`, `public/assets/site.css`, üretilen giriş sayfaları, README eşleri, bu iki dilli kayıt ve `tools/translation-pairs.json`.

Plan: girişte geliştirme durumunu görünür kılmak; birbirini tamamlayan üç ürünün rolünü açıklamak; uzmanlığın karşılığını anlatan abonelik bölümü eklemek; üst veriyi, SSS'yi ve topluluk metnini eşlemek; iki dili üretip doğrulamak; masaüstü/mobil gezinmeyi ve açılır yanıtları incelemek; öz inceleme ardından taslak PR teslim etmek. Mevcut bileşen kanıtlarının özgün inceleme tarihi ve kapsamı korunur. Yeni çalışma zamanı kabulü iddia edilmez.

## Kabul, risk ve bütçeler

- Ekosistem ve güncel geliştirme durumu: iki dilin giriş alanlarını ve üst verisini incelemek.
- Derleme: saha/sensör/makine verisini ve planlanan bulut ya da kurum içi kaydı, kaynak ve kalite bağlamıyla görünür kılmak.
- Onama: siber güvenliği, erişim yetkisini, sorumlulukları, denetim kayıtlarını ve mevzuata uyum süreçlerini sertifikasyon ya da uyum garantisi vermeden görünür kılmak.
- Abonelikler: herkese açık çekirdek bağımsız kullanılabilir kalır; ticari uzmanlık uydurma fiyat, paket, hizmet seviyesi veya ödeme imkânı sunmadan açıklanır.
- Doğrulama: katkı sözleşmesindeki tam komutlar, belirlenimci üretim/kontrol, incelenmiş EN/TR parmak izleri, doldurulmuş PR gövdesi kontrolü, tarayıcı kimliği/içerik/konsol/ekran görüntüleri, dil geçişi, abonelik gezinmesi, SSS ve mimari klavye davranışı.

Bütçe: 60 dakika, başarısız kapı başına en çok üç odaklı onarım; yeni bağımlılık, ücretli hizmet, görsel üretimi veya çalışma zamanı/model eğitimi yok. Riskler: ürün yönünü sunulmuş hizmetle karıştırmak, ortak markadan erişim yetkisi çıkarmak veya hukuki garanti vermek. Gelecek zaman anlatımı ve erişim sınırları korunur. Geri dönüş: kapsamlı site değişikliğini geri almak; veri taşıma yok.

## Roller ve kanıt

Mimar, uygulayıcı, doğrulayıcı ve öz incelemeci: Python, Git/GitHub CLI ve tarayıcı otomasyonu kullanan bu Codex GPT-6 oturumu. Ayrı incelemeci iddia edilmez. Browser eklentisi/becerisi yok; mevcut paketli çalışma ortamındaki Playwright kullanılır. Bağımsız/bakım sorumlusu incelemesi bekliyor. Yerel ve PR-CI sonuçları PR'da kaydedilir; site kontrolleri Rust, GPU, model, eğitim, saha kurulumu veya ticari hizmet kabulü oluşturmaz.

Yerel doğrulama: macOS arm64 ve Python 3.15.0 üzerinde (`python3` kullanan katkı komutları aynen çalıştırılarak) 54 depo testi, üretilen çıktı kontrolü, incelenmiş EN/TR parmak izleri, boş şablon yapısı ve boşluk kontrolü passed. Bağımlılık kurulmadı: hash kilitli CI envanteri yalnızca standart kütüphaneyi kullanır. CI ayrıca Python 3.14 kullanır. Tarayıcı doğrulaması: paketli Playwright 1.62.1 / Chromium ile iki dilde 1280 × 900 ve 390 × 844, ayrıca 320 piksel taşma kontrolü ve JavaScript kapalı abonelik/SSS kontrolleri passed. Denenen akış: giriş sayfası → abonelik gezinmesi → uzmanlık kapsamı ve geliştirme durumu; iki yönlü dil geçişi, ürün/topluluk gezinmesi, SSS açma/kapatma, Ata → Sağ Ok → İncele, yüklenen görseller ve sıfır konsol uyarısı/hatası. Masaüstü ürün/abonelik bölümleri ile mobil/masaüstü giriş görüntüleri görsel olarak incelendi; dosyalar deponun dışında tutuldu. Çalışma zamanı, bulut/kurum içi kurulum, hukuki uyum ve ücretli abonelikler: not_run, site görevinin dışında. PR CI ve bağımsız inceleme ayrı kapılardır.
