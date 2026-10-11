# Web sitesi tasarım tanımı

[English](design.md). `WEB-001 / 0.1.0`. Uygulama yönü yetkili geliştirme çalışması sırasında yazar tarafından seçildi; kullanıcı tasarım onayı iddia edilmez.

Dört Image Gen arayüz konsepti giriş, mimari, sorular/yanıtlar ve yol haritasını ayrı ayrı 1536 × 1024 boyutunda tanımlar. Bir ek yerleşik Image Gen çağrısı turuncu şerit heykelini ayırır. Bu görsel temsili sanat çalışmasıdır; ürün ekran görüntüsü değildir. Konseptler üretim dizini dışında, görüşme önizlemeleri olarak tutulur.

## Sistem

- Kâğıt `#F7F6F2`, mürekkep `#17252B`, turuncu `#EE5638`, diyagram zemini `#EFEDE7`, çizgi `#CFD2CF`. Küçük turuncu metinlerde kontrast için `#B63E28` kullanılır.
- Helvetica Neue, Helvetica, Arial, sans-serif; yazı tipi indirilmez. Konsept genişliğinde giriş başlığı 120px, ağırlık 750; bölüm başlığı 76px, gövde 23px, gezinme 18px. Duyarlı ölçekler hiyerarşiyi korur.
- En çok 1392px içerik; masaüstünde 72px, mobilde 24px kenar boşluğu. Bölümler arası 100–120px; ince çizgiler, 8px düğme/diyagram köşeleri, tekrarlanan kartlar yoktur.
- Konseptlerdeki hatalı logo benzetimleri yerine mevcut kanonik Eylema SVG logosu kullanılır; renkleri ve oranları korunur.
- Giriş görseli: kâğıt rengi üzerinde ayrı kare varlık; renk filtresi veya kaplama yok. Gerekirse yalnızca dış kenarları sayfaya karıştırılır. Metin ve bağlantılar HTML'dir.
- Simgeler: sağa ve sağ üste yönelen, 24px, 1.7px kalınlığında iki basit SVG ok; currentColor. Harici simge kütüphanesi yoktur.
- Hareket: kısa renk/alt çizgi geçişleri. Otomatik oynatma, kaydırma müdahalesi veya sürekli heykel animasyonu yoktur. Azaltılmış hareket tercihi geçişleri ve yumuşak kaydırmayı kapatır.

## Sayfa ve metin envanteri

1. Üst gezinme: Eylema logosu; Mimari, Yol haritası, GitHub; EN / TR. Giriş: “Niyetten / eyleme. / Tasarımla.” Ajan tabanlı web platformu vizyonu, mimariyi keşfet ve GitHub bağlantıları, görünür tasarım aşaması açıklaması. İlkeler: Açık bir tasarım; Temelinde yerel zekâ; Yönetim insanda.
2. Mimari: “Tek bir sözleşme. / Sürekli bir döngü.” Numaralı sekmeler: Tanımla, Geliştir, İşlet, Öğren. Varsayılan açıklama: “Niyetle başla.” Diyagramda Hedef; Durum, Eylemler, Yetki ve Bütçe ile bağlanır; önerilen uygulama sözleşmesi ve kavramsal gösterim olarak etiketlenir. Diğer sekmeler aynı bileşenle geliştirme, işletim ve izinli öğrenmeyi kaynaklara dayanarak açıklar. Alt çizgide insan yönlendirmesi vurgulanır.
3. Yol haritası: “Açıkça geliştir. / Adım adım doğrula.” Mimari/API tasarım aşaması; temel taslaklar, planlanan ilk uygulama ve öğrenme döngüsü için üç satır. Koyu katkı bandı ve gerçek GitHub deposu bağlantısı. Altbilgi: logo, tasarım ifadesi, mimari/API ve dil bağlantıları.

Alt bölümler aynı kenar boşluğunu, başlık ölçeğini ve açık çizgili düzeni paylaşır. Fiyatlandırma, panel, hesap, bekleme listesi veya model etkileşimi eklenmez. Mobil üst gezinme bağlantıları iki sade satırda gösterir. Sekmeler 2 × 2 olur; diyagram ve yol haritası dikeyleşir. Türkçe metin İngilizce satır uzunluklarına zorlanmadan anlam bakımından incelenir.

## Üretilen varlık istemi

Yerleşik Image Gen ile giriş konsepti referans alınarak yalnızca turuncu şerit heykeli ayrılır; arayüz ve metin kaldırılır. E benzeri üç katmanlı geometri, mat turuncu metal, önden/sağdan bakış, yumuşak temas gölgesi korunur. 1024 × 1024 kare, çevresinde yüzde 7 boşluk, kenarlara kadar `#F7F6F2` zemin istenir. Ürün çalışma kanıtı, metin veya filigran üretilmez. Tam İngilizce varlık istemi [kanonik belgede](design.md) bulunur.

Konsept istemleri metin envanterini, anlamsal HTML/CSS'yi, erişilebilir kademeli sekmeleri, kâğıt/mürekkep/turuncu paletini, açık bölümleri ve uydurma ürün kanıtlarının yasaklanmasını belirtir. Tam istemler ve üretilen önizlemeler görev görüşmesindedir.

## Kapsam eklemesi: uluslararası keşif

Proje sahibi SEO/GEO ve varsayılan İngilizce istedi. Dördüncü bölüm konsepti, mimari ve yol haritası arasına görünür, kaynaklı sorular/yanıtlar ekler: “Net bir fikir. / Dürüst bir başlangıç.” Dört doğal açılır kontrol; Eylema tanımını, bugünkü kullanılabilirliği, insan kontrolünü ve hedef platformları açıklar. İlk yanıt açıktır. Yol haritası etiketi 03 olur. Dört konsept ve varlık için toplam beş Image Gen çağrısı kullanılmıştır. Proje sahibi ayrı bir site deposu seçmiş, ardından son adını `eylema-dev/eylemadotdev` ve görünürlüğünü herkese açık olarak açıkça istemiştir.
