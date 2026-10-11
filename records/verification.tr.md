# Web sitesi doğrulaması

[English](verification.md). `WEB-001 / 0.2.0`, 11 Ekim 2026. Bu kaydı ekleyen PR başına uygulanır; tam commit ve CI çalışması PR içinde raporlanır. Taban: `a08b78d9210035aafdd2db35958f0c2d854c94c2`.

## Ortam ve roller

Yerel macOS, Python 3.14.8, CUA üzerinden Codex uygulama içi tarayıcısı, Git/GitHub CLI. Ek paketli Playwright Chromium 151.0.7922.34 yalnızca IAB içinde bulunmayan JavaScript kapatma ve azaltılmış hareket ayarları için kullanıldı. Sharp 0.35.5 özgün üretilmiş görseli kodladı. Site çalışma zamanı paketi kurulmadı. Mimar, uygulayıcı, doğrulayıcı ve öz incelemeci aynı Codex GPT-6 ailesi oturumudur; bağımsız incelemeci iddiası yoktur.

## Sonuçlar ve sınırlar

| Kontrol | Durum | Kanıt |
|---|---|---|
| AGENTS.md komutlarının tam sırası | passed | Sanal ortam, özet zorunlu boş bağımlılık kurulumu, 16 regresyon testi, depo denetleyicisi, boş PR şablonu ve fark boşluk kontrolü |
| Üretilen çıktı | passed | `tools/build.py --check`; İngilizce kök, Türkçe `/tr/`, güncel sitemap/robots/404 |
| İçerik ve keşfedilebilirlik | passed | JavaScript olmadan tam HTML; kendi canonical adresi, karşılıklı en/tr/x-default, metinle eşleşen JSON-LD, boyut/alt, bağlantılar, incelenmiş çeviri özetleri ve 35 KB CSS/JS bütçesi |
| Açık kaynak referansları | passed | 10 İngilizce/Türkçe kaynak belgenin platform deposu main ağacında bulunduğu doğrulandı |
| Depo değişikliği | passed | GitHub `eylema-dev/eylemadotdev` için PUBLIC bildiriyor; origin, proje sahibinin açık istekleriyle güncel adı kullanıyor |
| IAB etkileşimleri | passed | İngilizce/Türkçe bağlantıları, mimari düğmesi, dört sekme, seçili panel durumları, Home/End/ok tuşları, doğal soru açılması, Türkçe mobil öğrenme paneli |
| Duyarlı davranış | passed | EN: 320, 390, 768, 1024, 1536px; TR: 320, 390, 768, 1024px; yatay taşma yok; konsept boyutunda 1536 × 1024 görünüm denetlendi |
| Ek tarayıcı kipleri | passed | JavaScript kapalıyken iki dilde dört mimari paneli görünür; doğal sorular ve dil bağlantıları çalışır; azaltılmış harekette geçiş/yumuşak kaydırma yok; üçüncü taraf isteği veya sayfa hatası yok |
| Tarayıcı konsolu | passed | İzlenen IAB akışında uyarı/hata yok |
| Görsel sadakat | passed | Dört bölüm konsepti ve tarayıcı görüntüleri doğrudan `view_image` ile incelendi; aşağıdaki kayıt geçerlidir; çözülmemiş önemli fark yok |
| Bağımsız/proje sahibi incelemesi | not_run | Ayrı insan incelemesi gereklidir; öz inceleme ve CI yerine geçmez |
| Üretim barındırma, DNS/TLS, indeksleme, saha performansı | not_run | Sunucu kurulmadı veya dağıtım iddia edilmedi; yayına hazırlık listesi izlenmeli |
| Rust/GPU/model çalışma zamanı testleri | not_applicable | Bu depo yalnızca statik tanıtım sitesini uygular |

GitHub CI ve doldurulmuş PR metni kontrolü, ilgili PR içinde ayrı kanıtlardır. Yukarıdaki boş şablon sonucu doldurulmuş açıklamayı doğrulamaz. Ekran görüntüleri kaynak deposu dışında göreve bağlıdır; geçici QA betikleri yayınlanmaz.

## Görsel karşılaştırma kaydı

| Karşılaştırma | Konsept kanıtı | Tarayıcı kanıtı ve çözüm |
|---|---|---|
| Metin ve hiyerarşi | Üç satırlı “From intent / to action. / By design.”, iki eylem, görünür tasarım aşaması | İlk ekrandaki İngilizce metin birebir kontrol edildi; ek üst etiket, istatistik veya kanıt iddiası yok; Türkçe anlamı korur |
| Giriş düzeni ve görsel | Solda büyük metin, sağda turuncu şerit, altta ilkeler | Görselin doğal yüksekliği ve negatif yerleşimi düzeltilerek ilkeleri örtmesi engellendi; üst gezinme görsel kenarlarının üzerinde |
| Tipografi | Büyük sıkı başlıklar, bilinçli gövde/kontrol boyutları | Sistem Helvetica hiyerarşisi masaüstü/mobilde denetlendi; gerçek font ölçüleri ve Türkçe satırlar kasıtlı uyarlama |
| Palet ve varlık | Kâğıt/mürekkep/turuncu, filtresiz heykel | Hesaplanan kâğıt `#F7F6F2`, mürekkep `#17252B`, vurgu `#EE5638`; renk filtresi/kaplama yok, yalnızca kenar karışımı; küçük vurgu metni kontrast için koyu |
| Marka ve simgeler | Üretilmiş logo benzetimi, ince oklar ve açma simgeleri | Kanonik marka logosu kasıtlı olarak benzetimin yerini aldı; SVG oklar; açık sorunun simgesi eksiye düzeltildi |
| Mimari | Açık başlık, dört numaralı sekme ve sözleşme diyagramı | Dört çalışan durumda aynı bileşen; açık kavramsal/çalışma zamanı olmayan gösterim notu; gerçek kaynak bağlantıları |
| Sorular | Açık iki sütun, dört çizgili soru, ilk yanıt açık | Doğal kontroller, HTML içinde tam ve kaynaklı yanıtlar; istenen SEO/GEO ekinin ayrı dördüncü konsepti var |
| Yol haritası ve altbilgi | Üç durum satırı, koyu katkı bandı, sade altbilgi | Tasarım/plan durumları korundu, ilerleme ölçüsü uydurulmadı; sürekli sayfa boşlukları bölüm sistemini izler |
| Duyarlı düzen | Ortak boşluklar, açık bölüm ritmi ve hiyerarşi | İki satırlı mobil gezinme, dikey içerik ve 2 × 2 sekmeler; görsel/metin yatay taşma olmadan okunur |

Uygulamanın yazar tarafından seçilen dört konseptli tasarıma sadakati doğrulandı. Kalan kasıtlı farklar: kanonik logo, küçük metin için erişilebilir turuncu, gerçek sistem fontu/dil satırları ve ayrı üretilmiş heykelin küçük geometri farkıdır. Bunlar sayfa yapısını, iddiaları veya etkileşimleri değiştirmez. Kullanıcı tasarım onayı ima edilmez.
