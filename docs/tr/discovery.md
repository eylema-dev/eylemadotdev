# Arama görünürlüğü ve kaldırma

[English](../en/discovery.md). İnceleme: 14 Ekim 2026.

Bakım sorumlusu, mevcut `eylema.dev` sitesinin Google ve Bing sonuçlarından kaldırılmasını istedi. Site herkese açık kalır; aramadan çıkarma erişim denetimi değildir. Alan adı geçişi, DNS değişikliği, hesap/mülk silme veya doğrulama anahtarını kaldırma bu değişikliğe dâhil değildir.

İngilizce `/` ve Türkçe `/tr/` sayfaları `noindex,follow` bildirir. Azure'ın genel `X-Robots-Tag: noindex,follow` başlığı HTML, görseller ve diğer kaynakları kapsar. Özel 404 sayfası noindex kalır. Mevcut canonical/hreflang, sosyal üst veri, iki dilli içerik ve normal gezinme kullanılabilir.

`robots.txt`, arama motorlarının kaldırma yönergelerini alabilmesi için taramaya açıkça izin verir. Sitemap duyurmaz. Mevcut `/sitemap.xml`, daha fazla URL tanıtımını önlemek için boş URL kümesi içeren geçerli XML olarak kalır. Tarayıcıları engellemek noindex yönergesini görmelerini önler. [Google noindex rehberi](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [Azure yanıt başlıkları](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration).

## Gönderim ve sahiplik

IndexNow gönderimi herhangi bir ağ isteğinden önce devre dışı bırakılır. `tools/indexnow.py` yalnızca gönderim yapmadığını açıkça belirten önizlemeyi yazdırır; `--submit`, aramadan kaldırma ilkesi gerekçesiyle sıfırdan farklı kodla çıkar. Herkese açık sahiplik anahtarının baytları ve önceki gönderim alındıları tarihsel kanıt olarak korunur. Bu ilke geçerliyken indekslemeyi teşvik etmek için URL veya sitemap göndermeyin.

## Kabul ve izleme

1. Üretilen noindex üst verisini, genel başlıkları, taramaya izin veren robots dosyasını, boş sitemap'i ve gönderim reddini doğrulayın. Olumsuz testler indekslenebilir/çoğaltılmış/bota özel yönergeleri, başlık geçersiz kılmalarını, tarama engellerini ve yeniden URL tanıtımını reddeder.
2. Mevcut yetkili Azure kaynağını kullanarak yalnızca `public/` yayımlayın. Normal HTTPS, tam yayın commit'i, tüm kaynak özetleri/MIME, genel noindex başlıkları, yönlendirme ve gerçek 404 doğrulanır. Yerel `http.server`, Azure başlıklarını uygulamaz; kaynak kontrolü başlığın yayımlandığının kanıtı değildir.
3. Google Search Console ve Bing Webmaster mülkleri ile inceleme erişimini koruyun. Ayrı yetkilendirilmiş sahip paneli kaldırma istekleri geçici işlemlerdir; gerçek kapsam/durumları geri okunmalıdır. [Google kaldırma aracı](https://support.google.com/webmasters/answer/9689846?hl=en), [Bing URL engelleme](https://www.bing.com/webmasters/help/?topicid=264e560a).
4. Üç ayrı durumu kaydedin: yayımlanmış kalıcı noindex, geçici kaldırma isteğinin durumu ve gözlenen arama motoru indeksleme durumu. Yüklenmiş çıktı veya kabul edilen kaldırma isteği nihai kaldırmayı kanıtlamaz. Arama motorları değişiklikleri eşzamansız işler.

14 Ekim 2026 doğrulamasında canonical alan adının DNS'i NXDOMAIN döndürüyor. Azure yüklemesi başarılı olurken normal canonical doğrulaması başarısız olabilir. Alan adı kararları ertelendi; hatayı görünür tutun, DNS'i ve mevcut yönlendirmeleri değiştirmeyin. Alan adı çözülene kadar tarayıcılar yönergeleri gözleyemez. [Güncel kaldırma kaydına](../../records/search-removal.tr.md) bakın. İndekslemeyi geri açmak veya gönderimleri sürdürmek için ileride doğrudan bakım sorumlusu kararı gerekir.
