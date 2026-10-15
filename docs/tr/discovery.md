# Arama görünürlüğü ve kaldırma

[English](../en/discovery.md). İnceleme: 14 Ekim 2026.

Bakım sorumlusu, mevcut `eylema.dev` sitesinin Google ve Bing sonuçlarından kaldırılmasını istedi. Site herkese açık kalır; aramadan çıkarma erişim denetimi değildir. İlk 14 Ekim kaldırma değişikliği; alan adı geçişi, DNS değişikliği, hesap/mülk silme ve doğrulama anahtarı kaldırmayı kapsamıyordu. Sonraki adres değişikliği için aşağıdaki alan adı hazırlığı kararına bakın.

İngilizce `/` ve Türkçe `/tr/` sayfaları `noindex,follow` bildirir. Azure'ın genel `X-Robots-Tag: noindex,follow` başlığı HTML, görseller ve diğer kaynakları kapsar. Özel 404 sayfası noindex kalır. Mevcut canonical/hreflang, sosyal üst veri, iki dilli içerik ve normal gezinme kullanılabilir.

`robots.txt`, arama motorlarının kaldırma yönergelerini alabilmesi için taramaya açıkça izin verir. Sitemap duyurmaz. Mevcut `/sitemap.xml`, daha fazla URL tanıtımını önlemek için boş URL kümesi içeren geçerli XML olarak kalır. Tarayıcıları engellemek noindex yönergesini görmelerini önler. [Google noindex rehberi](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [Azure yanıt başlıkları](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration).

## Gönderim ve sahiplik

IndexNow gönderimi herhangi bir ağ isteğinden önce devre dışı bırakılır. `tools/indexnow.py` yalnızca gönderim yapmadığını açıkça belirten önizlemeyi yazdırır; `--submit`, aramadan kaldırma ilkesi gerekçesiyle sıfırdan farklı kodla çıkar. Herkese açık sahiplik anahtarının baytları ve önceki gönderim alındıları tarihsel kanıt olarak korunur. Bu ilke geçerliyken indekslemeyi teşvik etmek için URL veya sitemap göndermeyin.

## Kabul ve izleme

1. Üretilen noindex üst verisini, genel başlıkları, taramaya izin veren robots dosyasını, boş sitemap'i ve gönderim reddini doğrulayın. Olumsuz testler indekslenebilir/çoğaltılmış/bota özel yönergeleri, başlık geçersiz kılmalarını, tarama engellerini ve yeniden URL tanıtımını reddeder.
2. Mevcut yetkili Azure kaynağını kullanarak yalnızca `public/` yayımlayın. Normal HTTPS, tam yayın commit'i, tüm kaynak özetleri/MIME, genel noindex başlıkları, yönlendirme ve gerçek 404 doğrulanır. Yerel `http.server`, Azure başlıklarını uygulamaz; kaynak kontrolü başlığın yayımlandığının kanıtı değildir.
3. Google Search Console ve Bing Webmaster mülkleri ile inceleme erişimini koruyun. Ayrı yetkilendirilmiş sahip paneli kaldırma istekleri geçici işlemlerdir; gerçek kapsam/durumları geri okunmalıdır. [Google kaldırma aracı](https://support.google.com/webmasters/answer/9689846?hl=en), [Bing URL engelleme](https://www.bing.com/webmasters/help/?topicid=264e560a).
4. Üç ayrı durumu kaydedin: yayımlanmış kalıcı noindex, geçici kaldırma isteğinin durumu ve gözlenen arama motoru indeksleme durumu. Yüklenmiş çıktı veya kabul edilen kaldırma isteği nihai kaldırmayı kanıtlamaz. Arama motorları değişiklikleri eşzamansız işler.

14 Ekim 2026 doğrulamasında canonical alan adının DNS'i NXDOMAIN döndürüyor. Azure yüklemesi başarılı olurken normal canonical doğrulaması başarısız olabilir. O tarihsel çalışmada alan adı kararı ertelenmişti. Proje sahibi sonrasında eski alan adını kapattı; yeni kimlik aşağıda açıklandığı gibi henüz yayımlanmadı. Alan adı çözülene kadar tarayıcılar yönergeleri gözleyemez. [Güncel kaldırma kaydına](../../records/search-removal.tr.md) bakın. İndekslemeyi geri açmak veya gönderimleri sürdürmek için ileride doğrudan bakım sorumlusu kararı gerekir.

## Alan adı hazırlığı — 15 Ekim 2026

Proje sahibi artık eyleme.dev adresini seçti ve eylema.dev adresini kapattı. Yeni alan adı satın alınmadı. [Kimlik geçişi](../../records/website-identity.tr.md) yeni sunucu için canonical, karşılıklı dil ve sosyal metaverileri hazırlar; yayın veya DNS değişikliği yapmaz. Bu, yukarıdaki ertelenmiş alan adı kararının yerini alır. Açık bir indeksleme kararı verilene kadar noindex, boş sitemap ve kapalı gönderimler korunur. Eski alan adının kaldırılma raporları ayrı tarihsel ve izleme kanıtı olarak kalır. Yeni alan adı için yönetim paneli doğrulaması ve canlı sunucu kanıtı henüz yoktur.

## Satın alınmış alan adı açılışı — 15 Ekim 2026

Proje sahibi artık eyleme.dev adresini GoDaddy’den aldı ve mevcut Azure sitesine bağlanmasını açıkça istedi. Bu, satın alınmamış alan adı hazırlık notunun yerini alır. [Alan adı açılış kaydı](../../records/eyleme-domain.tr.md); DNS sahipliği/yönlendirmesi, sertifikalar, yönlendirmeler, yayımlanan sürüm kimliği ve tarayıcı kanıtını ayrı tutar. Mevcut noindex/boş sitemap/kapalı gönderim politikası geçerlidir; yeni alan adını almak veya bağlamak arama gönderimlerini yeniden açma yetkisi değildir. Eski alan adını kaldırma takibi ayrı kalır.
