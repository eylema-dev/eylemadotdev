# Arama keşfi

[English](../en/discovery.md). İnceleme: 15 Ekim 2026.

Proje sahibi https://eyleme.dev/ adresinin Google Search Console ve Bing Webmaster Tools'a eklenmesini, sitemap gönderimini ve İngilizce/Türkçe indeksleme isteklerini açıkça istedi. Bu karar yeni alana devralınan dışlama politikasının yerini alır; eski eylema.dev kaldırma raporlarını veya takiplerini iptal etmez ya da değiştirmez. [WEB-020](../../records/search-launch.tr.md) ve tarihsel [kaldırma kaydına](../../records/search-removal.tr.md) bakın.

## Taranabilir canonical sayfalar

İngilizce https://eyleme.dev/ ve Türkçe https://eyleme.dev/tr/ index,follow, kendi canonical adresleri ve karşılıklı en/tr/x-default bağlantıları bildirir. Azure'da genel X-Robots-Tag dışlaması veya rotaya özel bot kuralı yoktur. Gerçek HTTP404 belgesi noindex kalır. robots.txt taramaya izin verir, https://eyleme.dev/sitemap.xml adresini duyurur. XML sitemap tam iki canonical sayfayı ve gerçek değişiklik tarihlerini içerir; üretimler yeni tarih uydurmaz. www ve Azure adresi yolu koruyarak canonical köke yönlenir. [Google sitemap rehberi](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Google noindex rehberi](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

## Sahiplik ve gönderim

Yeni mülk mevcut sahip oturumundan eklenir, yalnız motorun verdiği açık sahiplik kanıtı doğrulanır, sitemap gönderilir. Google Domain doğrulaması yeni GoDaddy TXT kaydı gerektirebilir; mevcut Azure, e-posta ve DNS kayıtları korunur. Bing yeni geniş hesap izinleri vermeden sunduğu doğrulama yöntemlerini kullanabilir. Her canonical URL motora bir kez gönderilir; tekrarlar hız garantisi vermez. İlk arama açılışı sahip panosu gönderimlerini kullandı; daha sonraki açık IndexNow isteği aşağıda uygulanır. Tarihsel sahiplik baytları/alındılar değişmez. [Bing doğrulama](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b), [Bing sitemap](https://www2.bing.com/webmasters/help/sitemaps-3b5cf6ed), [Bing URL gönderimi](https://www.bing.com/webmasters/help/URL-Submission-62f2860b).

## Kanıt sınırı

Kaynak/canlı eşikleri noindex giriş sayfalarını, engelleyici veya çelişkili yanıt başlıklarını, tarama engellerini, eksik/yinelenen/yabancı sitemap adreslerini ve eski tarihleri reddeder. Tam yayın kimliği, dosya envanteri/özet/MIME, güvenlik başlıkları, gerçek404 ve dil yönlendirmeleri zorunludur.

Mülk sahipliği, sitemap işlenmesi ve URL istek kabulü gerçek panolardan geri okunur. Yalnız Google Index / Bing Index URL Inspection açıkça indekslendi diyorsa indeksleme kanıtıdır; canlı test, sitemap keşfi veya kabul edilmiş istek değildir. Motorlar neyi ne zaman indeksleyeceğine karar verir. Güncel durum dürüstçe kaydedilir; kullanıcı işlemi isteyen oturum/CAPTCHA veya erişilemeyen pano, erişim engelidir ve indekslenmeme kanıtı değildir. Otomatik takip açıkça istenmiş bir izleyici gerektirir; eski alan takipleri sessizce değiştirilmez.

## IndexNow — 15 Ekim 2026

Proje sahibi artık eyleme.dev için IndexNow'u açıkça yetkilendirdi; bu karar yeni alan için önceki kapalı araç politikasının yerini alır. Mevcut kök UTF-8 sahiplik dosyası korunur. [Etkinleştirme kaydı](../../records/eyleme-indexnow.tr.md) sınırlı kapsamı ve [resmi yanıt anlamlarını](https://www.indexnow.org/documentation) belirtir.

`.venv/bin/python tools/indexnow.py` tam iki canonical URL'yi ağ erişimi olmadan önizler. `.venv/bin/python tools/indexnow.py --submit --receipt /tmp/eyleme-indexnow-receipt.json` önce normal HTTPS200, tam text/plain anahtar baytları, indekslenebilir sayfa üst verisi ve kendi canonical adreslerini kontrol eder; sonra https://api.indexnow.org/indexnow adresine tek JSON POST gönderir. Alındılar depo dışında tutulur; mevcut alındı yolu gönderimden önce durur. Yönlendirmeler kapalıdır; hata/429 otomatik tekrarlanmaz. Yinelenen veya ilgisiz dağıtım gönderimi eklenmedi.

HTTP200 başarılı gönderimi onaylar. HTTP202 alındıyı ve bekleyen anahtar doğrulamasını belirtir; açık anahtar dosyasının200 dönmesi tek başına motor tarafı doğrulamayı kanıtlamaz. HTTP403/422 sahiplik/şema hatasıdır,429 bekleme gerektirir. Alındıların hiçbiri tarama/indekslenme kanıtı değildir. Mevcut salt okunur Google/Bing indeksleme takipleri ayrı kalır; bu komut kendiliğinden yeni takip açmaz.
