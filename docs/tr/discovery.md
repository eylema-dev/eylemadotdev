# Uluslararası arama ve üretken keşif

[English](../en/discovery.md). 13 Ekim 2026'da incelendi.

Varsayılan, coğrafi kısıtı olmayan İngilizce `/`, Türkçe `/tr/` adresindedir. Her sayfa kendi canonical adresini, iki dili ve İngilizce `x-default` değerini belirtir. Tarayıcı diline veya ülkeye göre otomatik yönlendirme yoktur. Tam metin, kaynaklar ve yanıtlar ilk HTML cevabındadır. `robots.txt` taramaya izin verir ve iki sayfalık sitemap'e işaret eder. Open Graph ve sosyal kartlar gerçek marka görselini kullanır.

JSON-LD; Eylema'yı Organization/proje, WebSite ve kaynak atıflı WebPage olarak tanımlar. Kuruluş, yayınlanmış SoftwareApplication, fiyat, puan, performans veya müşteri iddiası içermez. Gizli içerik, anahtar kelime doldurma veya uydurma destek yoktur. Görünür metin ve metadata, uygulanmış yerel görev temelini önerilen işbirlikçi döngü/model/eğitim entegrasyonlarından ayırır. Güncel iki dilli v0.7 görseli; platformu, isteğe bağlı rolleri, proje RAG/belleğini ve yerel eğitim planını açık entegrasyon-tasarımı bildirimi ve anlamlı alt metinleriyle gösterir. Bileşen kanıtı ve sınırlı native insan kabulü ayrı atıflanır; bunlardan çıkarım, tam ürün veya performans iddiası doğmaz.

Google'ın güncel rehberi, temel SEO ilkelerini üretken aramaya uygular. Özel AI işaretlemesinin ve `llms.txt` dosyasının Google Search için gerekli olmadığını ve Google sıralamasını iyileştirmediğini açıkça belirtir. Bu nedenle özgün proje bilgisine, kaynaklara, açık dile, taranabilirliğe ve kullanılabilir sayfalara öncelik verilir. Özel AI dosyası veya FAQ zengin sonucu vaadi gerekmez. [Google üretken AI rehberi](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [yerelleştirilmiş sayfalar](https://developers.google.com/search/docs/specialty/international/localized-versions), [kuruluş verisi](https://developers.google.com/search/docs/appearance/structured-data/organization).

## Yayına kabul

1. Barındırma yetkisiyle **yalnızca `public/`** yayınlanır. GitHub kaynağı proje sahibinin isteğiyle herkese açıktır; web sunucusuna yalnızca site çıktısı konur. `eylema.dev` HTTPS'i kurulur; diğer sunucu adları ve HTTP, seçilen canonical HTTPS adresine yönlendirilir.
2. `/` ve `/tr/` HTTP 200, varlıklar doğru MIME, eksik yollar gerçek HTTP 404 ve `404.html` ile sunulur. Genel SPA fallback kullanılmaz. Tekrarlanan `/index.html` biçimleri sunucuda dizin adreslerine yönlendirilir.
3. HTML, CSS/JS, sitemap ve robots için yeniden doğrulama kullanılır. Varlık adları içerik özeti taşımadığı için immutable önbelleğe alınmaz. Sıkıştırma, TLS, güvenlik başlıkları ve CDN sunucu ayarlarıdır; yerelde doğrulanmış değildir.
4. Yayınlanan tam revizyon, iki dil, canonical/hreflang, JSON-LD, robots/sitemap, hata yolu ve duyarlı tarayıcı davranışı yerel çıktıyla karşılaştırılır. Lighthouse/PageSpeed ve daha sonra saha Core Web Vitals ölçülür; yerel boyut bütçesi saha sonucu değildir.
5. Hesap/alan adı yetkisiyle Google Search Console ve Bing Webmaster Tools doğrulanır, sitemap gönderilir, iki URL incelenir ve Search Console'daki üretken aramaya dahil olma kontrolleri değerlendirilir. Doğrulama anahtarı uydurulmaz; gönderilen URL indekslenmiş sayılmaz.

## IndexNow bildirimleri

`tools/build.py` içindeki `PAGE_MODIFIED`, her dildeki sayfanın gerçek değişiklik tarihini kaydeder. Görünür tasarım inceleme tarihinden bağımsız olarak sitemap `lastmod` ve WebPage `dateModified` alanlarını besler. Yalnızca gerçekten değişen sayfanın kaydını güncelleyin; mevcut derleme/dağıtım zamanını kullanmayın. Canlı revizyonu doğruladıktan sonra aşağıdaki değişiklik bildirimini bir kez gönderin. [Bing güncellik rehberi](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/).

Üretici, `tools/build.py` içindeki `INDEXNOW_KEY` değerinden kökte UTF-8 sahiplik dosyası oluşturur. Anahtar herkese açık doğrulama verisidir; hesap kimlik bilgisi değildir. Üretilen çıktı kontrolleri eksik veya değişmiş içeriği reddeder; yayın manifesti ve canlı kontrol dosya özetini ve `text/plain` MIME türünü kapsar.

Sayfalardan birindeki değişikliği yayınladıktan sonra sabit iki sayfalık gönderimi önizleyip bir kez gönderin:

```sh
.venv/bin/python tools/indexnow.py
.venv/bin/python tools/indexnow.py --submit
```

Gönderim komutu önce canlı anahtar baytlarını ve iki canonical HTTP 200 adresini kontrol eder, ardından `https://api.indexnow.org/indexnow` adresine tek JSON POST gönderir. Doğrulama veya HTTP hatasında durur; otomatik tekrar denemez. HTTP 200 alındıyı, 202 ise alındı ile bekleyen anahtar doğrulamasını belirtir. Hiçbiri tarama, indeksleme veya sıralama kanıtı değildir. Anahtarı kullanırken dosyayı yayında tutun. [IndexNow protokolü](https://www.indexnow.org/documentation).

Bildirim katılımcı arama motorlarına ulaşır; Search Console veya sitemap'in yerini almaz. Google ve Bing indeksleme durumu kendi webmaster araçlarında kontrol edilmelidir. İndekslemeyi zorlamak için periyodik değil, gerçek sayfa değişikliklerinde gönderin.

## Uluslararası tanınırlığı geliştirmek

Kanıt taşıyan yararlı İngilizce güncellemeler ve Türkçe eşlikçileri yayınlanır: bir mimari karar açıklanır, ilk gerçek uygulama çalıştığında anlatılır, ölçülmüş performans tekrar üretilebilir biçimde sunulur, kabul edilmiş değişikliklerin sınırları belgelenir. Her kapsamlı yeni makalede kalıcı adres, yazar/proje atfı, gerçek güncelleme tarihi ve kanıt bağlantıları bulunur. Yüzeysel dil veya anahtar kelime sayfaları topluca üretilmez.

İndeksleme sonrası temel ölçümler kaydedilir: markalı/markasız gösterim ve tıklama, ülke/dil, indekslenen sayfalar, atıf veren yayınlar, yönlendirme trafiği ve nitelikli GitHub katkıları. Mevcut Search Console arama/üretken raporlarının kapsamı ve tarihi belirtilir. Büyüme yalnızca etiketlerle değil, süren özgün çalışma ve dağıtımla sağlanır. Tanıtım mesajları, sosyal paylaşımlar, analitik ve zamanlanmış izleme ayrı yetkili işlerdir. Sıralama, atıf ve dünya çapında tanınırlık ölçülecek sonuçlardır; garanti değildir.
