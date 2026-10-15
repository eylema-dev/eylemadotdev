# Arama keşfi

[English](../en/discovery.md). İnceleme: 15 Ekim 2026.

Proje sahibi https://eyleme.dev/ adresinin Google Search Console ve Bing Webmaster Tools'a eklenmesini, sitemap gönderimini ve İngilizce/Türkçe indeksleme isteklerini açıkça istedi. Bu karar yeni alana devralınan dışlama politikasının yerini alır; eski eylema.dev kaldırma raporlarını veya takiplerini iptal etmez ya da değiştirmez. [WEB-020](../../records/search-launch.tr.md) ve tarihsel [kaldırma kaydına](../../records/search-removal.tr.md) bakın.

## Taranabilir canonical sayfalar

İngilizce https://eyleme.dev/ ve Türkçe https://eyleme.dev/tr/ index,follow, kendi canonical adresleri ve karşılıklı en/tr/x-default bağlantıları bildirir. Azure'da genel X-Robots-Tag dışlaması veya rotaya özel bot kuralı yoktur. Gerçek HTTP404 belgesi noindex kalır. robots.txt taramaya izin verir, https://eyleme.dev/sitemap.xml adresini duyurur. XML sitemap tam iki canonical sayfayı ve gerçek değişiklik tarihlerini içerir; üretimler yeni tarih uydurmaz. www ve Azure adresi yolu koruyarak canonical köke yönlenir. [Google sitemap rehberi](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Google noindex rehberi](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

## Sahiplik ve gönderim

Yeni mülk mevcut sahip oturumundan eklenir, yalnız motorun verdiği açık sahiplik kanıtı doğrulanır, sitemap gönderilir. Google Domain doğrulaması yeni GoDaddy TXT kaydı gerektirebilir; mevcut Azure, e-posta ve DNS kayıtları korunur. Bing yeni geniş hesap izinleri vermeden sunduğu doğrulama yöntemlerini kullanabilir. Her canonical URL motora bir kez gönderilir; tekrarlar hız garantisi vermez. IndexNow kapalı kalır; bu açılış açıkça istenen sahip panosu gönderimlerini kullanır. Tarihsel sahiplik baytları/alındılar değişmez. [Bing doğrulama](https://www2.bing.com/webmasters/help/add-and-verify-site-12184f8b), [Bing sitemap](https://www2.bing.com/webmasters/help/sitemaps-3b5cf6ed), [Bing URL gönderimi](https://www.bing.com/webmasters/help/URL-Submission-62f2860b).

## Kanıt sınırı

Kaynak/canlı eşikleri noindex giriş sayfalarını, engelleyici veya çelişkili yanıt başlıklarını, tarama engellerini, eksik/yinelenen/yabancı sitemap adreslerini ve eski tarihleri reddeder. Tam yayın kimliği, dosya envanteri/özet/MIME, güvenlik başlıkları, gerçek404 ve dil yönlendirmeleri zorunludur.

Mülk sahipliği, sitemap işlenmesi ve URL istek kabulü gerçek panolardan geri okunur. Yalnız Google Index / Bing Index URL Inspection açıkça indekslendi diyorsa indeksleme kanıtıdır; canlı test, sitemap keşfi veya kabul edilmiş istek değildir. Motorlar neyi ne zaman indeksleyeceğine karar verir. Güncel durum dürüstçe kaydedilir; kullanıcı işlemi isteyen oturum/CAPTCHA veya erişilemeyen pano, erişim engelidir ve indekslenmeme kanıtı değildir. Otomatik takip açıkça istenmiş bir izleyici gerektirir; eski alan takipleri sessizce değiştirilmez.
