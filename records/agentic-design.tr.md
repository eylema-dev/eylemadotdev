# İnsan yönetiminde eylemci ekosistem tasarımı

[English](agentic-design.md). WEB-026 sürüm 0.1.0, 15 Ekim 2026.

Yetki: bakım sorumlusu eylemci yapay zekâ, güncel ve yerel modeller, model reçeteleri, işleri yürüten ve geliştiren eylemciler ile human-in-the-loop, human-on-the-loop ve human-in-command odaklı fütüristik açık/koyu site tasarımını doğrudan istedi. Uzmanlık ekibinin kurulmakta olduğunu, saha desteğinin planlandığını netleştirdi. Yayın, bu konuşmadaki açık site teslim yetkisinin devamıdır.

Taban: güncel `origin/main` olan `ce7ca50e8992a2eb0b067a69898aeba65570b06a`; dal `codex/agentic-light-dark-design`. İzinli yollar: iki dilli içerik, `tools/build.py`, tema/başlangıç betikleri ve stil dosyası, üretilen sayfalar/üçgen çeşitleri, gerekirse genel varlık envanteri, odaklı tema/içerik testleri, README/araç belgeleri, bu iki dilli kayıt ve çeviri parmak izleri.

Plan: görsel üretimle tasarım referansları oluşturmak, ortak renk ve duyarlı bileşenleri tanımlamak, erişilebilir açık/koyu geçişi eklemek, model/reçete ve insan kontrolü anlatısını güçlendirmek, kurulmakta olan Derleme/Onama uzmanlık ekibini uçtan uca saha teslim akışıyla anlatmak. Tam sloganları, mobilde sloganın hemen altındaki üçgeni, açık kaynak/topluluk ve ücretli/geliştirme sınırlarını korumak. Mevcut kanıtları ve kaynak bağlantılarını gelecek ürün yönünden ayrı sunmak. Model adları veya performans iddiaları uydurulmaz.

Kabul: okunabilir TR/EN açık/koyu masaüstü ve mobil görünümler; sistem varsayılanı ve hatırlanan tercih kullanan, klavyeyle çalışabilen tema düğmesi; depolama engeli ve JavaScript kapalı durumlarda uygun davranış; tema parlaması veya yinelenen duyuru olmaması; temayla uyumlu üçgen/marka varlıkları; çalışan dil, SSS ve mimari etkileşimleri; taşma veya konsol hatası olmaması. Katkıcı kapıları, belirlenimci üretim, gözden geçirilmiş çeviri parmak izleri, anlamlı yeni hata kapsamı ve doldurulmuş PR doğrulaması çalıştırılır. Sınırlı fark öz incelemeden geçirilir, PR/main kontrolleri tam sürümde geçer, Azure/kanonik yayın ve tarayıcı temizliğe geçmeden doğrulanır.

Bütçe: 90 dakika, dört ana tasarım görseli ve en çok iki odaklı iyileştirme, başarısız kapı başına üç odaklı onarım. Yeni üretim paketi, sağlayıcı API'si, ücretli altyapı, DNS veya izin değişikliği yoktur. Ana riskler: koyu tema kontrastı, kanıtsız hizmet/model iddiaları, aşırı içerik yoğunluğu, tema tercihi ve duyarlı yerleşim. Geri dönüş: bu sınırlı sürümü geri alıp yeniden yayımlamak.

Roller: bu Codex GPT-6 oturumu mimar, uygulayıcı, doğrulayıcı ve öz inceleyicidir; araçlar Image Gen, Python, Git/GitHub CLI, tarayıcı otomasyonu ve Azure CLI'dır. Bağımsız inceleyici iddiası yoktur. Mevcut SVG marka/üçgen varlıkları yerel vektör olarak kalır; tasarım görselleri referanstır, yayımlanan arayüz değildir. İki dil ve görsel durumlar ayrı incelenir. Site kanıtı model çalıştırma, eğitim, saha kabulü veya ticari kullanılabilirlik değildir.

İnsan kontrolü metni bir ürün tasarımı yorumudur: seçili adımlarda onay, müdahale edilebilen gözetim ve hedef/sınır/yayın kararlarında insan yetkisi. Kaynak: insan gözetimi rollerinin ayrımı için [NIST AI RMF Core, GOVERN 3.2](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Mevzuata uyum veya sertifika iddiası değildir.

## Tasarım belirtimi

Dört yerleşik Image Gen referansı koyu/açık giriş, model/kontrol ve saha teslim bölümlerini tanımlar. Renkler: soğuk açık `#f5f8fa`, metin `#10252e`, ikincil `#526875`, turuncu `#ce492c`, petrol `#167685`; koyu `#0b1116`, metin `#edf3f7`, ikincil `#a4b5bf`, turuncu `#ff714e`, camgöbeği `#84d8e2`, bant `#111c24`. Yazı sistemi mevcut sistem Helvetica ailesini, güçlü sıkı başlıkları, 18–22px okunabilir gövdeyi, küçük eş aralıklı sıra etiketlerini ve belirgin düğme metinlerini kullanır. İnce çizgiler, dairesel şema düğümleri ve açık sütunlar bileşen dilini oluşturur. Üst çubuk, model listesi, üç gözetim sütunu, saha teslim hattı ve mevcut alt bölümler ortak hizalama ve boşluklar kullanır. Hareket yalnızca kontrol durumu geçişlerindedir ve azaltılmış hareket tercihini izler.

İzinli giriş metni: mevcut tam sloganlar; geliştirme durumu; insan yönetimindeki eylemci ekosistem açıklaması; ekosistem/kaynak eylemleri; üç ürün adı, veri/yetki/geri bildirim ve insan kontrolü etiketleri; geliştirme açıklaması. Gezinme ekosistem, insan kontrolü ve topluluğa gider; tema ve dil kontrolleri açıktır. Model satırları ile gözetim/saha metinleri kabul edilen istek ve kurulmakta olan ekip açıklamasına dayanır.

Üretilen referanslara bilinçli düzeltmeler: özgün Eyleme kelime logosunun biçimini korumak; doğru Derleme → Onama veri, Onama → Eyleme yetki ve Eyleme → Derleme geri bildirim yönlerini tutmak; uydurulmuş süs sloganlarını/alan adlarını ve bugün hizmet verildiği izlenimini çıkarmak; raster maket yerine mevcut düzenlenebilir vektör sistemini kullanmak. Önceki kapsamlı mimari kanıt, SSS, yol haritası, topluluk ve abonelik içeriği aynı yazı sisteminde kalır. Mevcut alt bölümlerin görünümü yenilenir; uydurma ürün ekranlarıyla değiştirilmez. Mobilde kabul edilmiş slogan → üçgen → açıklama sırası korunur. Üretilen tasarım görselleri sayfa arayüzü olarak yayımlanmaz.

## Görsel uyum incelemesi ve yerel kanıt

Kontrol edilen akış: her yerelleştirilmiş giriş sayfası → tema, dil, gezinme, SSS ve mimari denetimleri → planlanan yetenek bildirimleri korunurken okunabilir içerik ve beklenen durum.

| Referans özelliği | Uygulanan karar ve inceleme |
|---|---|
| Grafit / soğuk açık palet | İki tema belirlenen renkleri ve turuncu/camgöbeği vurgularını kullanır; uygulama içi tarayıcıda incelendi |
| Kompakt, büyük üç satırlı slogan | Tam EN/TR sloganları korundu; ölçek geliştirme durumu ve eylemleri görünür tutacak şekilde ayarlandı |
| İnsan merkezli dairesel üçgen | Özgün duyarlı SVG, onaylı veri/yetki/geri bildirim yönlerini korur; büyük mobil etiketler tekrarlanan ikincil ayrıntıyı gizler, alternatif metin ve ürün açıklaması korur |
| Model satırları ve insan kontrolü bandı | Üç numaralı model satırı, altı iş akışı aşaması ve üç ayrı gözetim sütunu konsept hiyerarşisini izler |
| Saha akışı ve ürün çizimleri | Dört aşamalı hat ve özgün sensör/bulut, kalkan ve katmanlı topluluk çizimleri fiziksel/dijital bağı gösterir; soyut görseller kurulu saha iddiası taşımaz |
| Gezinme, kelime logosu ve destekleyici içerik | Özgün logo silueti korundu; üç gezinme bağlantısı tema/dil kontrollerinin yanında; mevcut kanıt bölümleri yeni tipografiyi paylaşır |

İlk ekran metin incelemesi: üretilen referanslardaki uydurma dekoratif slogan veya alan adı yayımlanmıyor. İstenen slogan, insan kontrollü giriş, geliştirme durumu, iki eylem ve yerelleştirilmiş şema etiketleri/açıklaması mevcut. Mevcut kapsamı ayıran temel durum cümlesi görünür kalır. Üretilmiş manzara ve fotoğraf iddiaları bilinçli olarak kullanılmadı; özgün ürün çizimleri saha/güvenlik/topluluk motifini sağlar. İncelenen masaüstü/mobil durumlarda çözülmemiş önemli görsel uyumsuzluk bulunmadı.

Bu PR çalışma revizyonunda macOS arm64 / Python 3.15.0 ile yerel kontroller geçti: altı yeni olumsuz eşik testi dahil 62 birim testi, deterministik derleme, depo doğrulaması, incelenmiş çeviri parmak izleri ve fark boşluk denetimi. CSS ve JavaScript, 35 KB ham bütçenin altında. Uygulama içi tarayıcıda EN/TR × açık/koyu × 320, 390, 720, 721, 768, 1024, 1280, 1440px olmak üzere 32 yerleşimde yatay taşma bulunmadı; mobil slogan → üçgen → giriş sırası geçti. Klavye tema geçişi, dilde tercih kalıcılığı, mimari ok tuşları, varlıklar ve konsol kontrol edildi.

Uygulama içi tarayıcının sunmadığı koşullar için paketli Playwright kullanıldı: sistem rengi değişimi, JavaScript kapalı, engelli/geçersiz yerel depolama ve azaltılmış hareket. Bu yedeklerin yanı sıra yenileme/dil/sekmeler arası tercih kalıcılığı, gezinme, SSS, klavye sekmeleri, yüklü varlıklar ve ilk içerik boyamasından önce kayıtlı koyu tercih dahil 11 senaryo geçti. Bu, her tarayıcının veya fiziksel telefonun test edildiği iddiası değildir. CI, üretim ve kanonik canlı kanıt, çalıştırıldıktan sonra teslim PR’ında ayrıca kaydedilir.

## Geometri düzeltmesi

WEB-026 revizyon 0.2.0, birleştirilmiş main `79e9eaa9e49abe6361f6c9dc9edaa83703eab885` temeli, `codex/agentic-diagram-polish` dalı. Son ürün çizimi incelemesinde Derleme bulutunun viewBox üstüne 5,01 SVG birimi taştığı görüldü. Metni ve çevre şemayı koruyarak bulut yolunu 8 birim aşağı kaydır. İzinli yollar: derleyici, üretilen EN/TR HTML, bu kayıt ve çeviri parmak izleri. Bütçe: ilk web sitesi yayın yetkisi içinde tek odaklı düzeltme ve 15 dakika. Kabul: üç ürün çizimi de çizgi payıyla viewBox içine sığmalı; derleme/depo/katkı eşikleri, tam PR/main revizyonunda CI ve son canlı doğrulama. Aynı uygulayıcı/doğrulayıcı/öz incelemeci; ayrı incelemeci iddiası yok.
