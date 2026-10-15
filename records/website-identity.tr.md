# Site kimliği geçişi

Görev WEB-017, revizyon 0.1.0, 15 Ekim 2026. Main tabanı: `81410a45c4cdd0ad8176e775f284e488fa11dc1d`. Dal: `codex/eyleme-website-identity`.

Yetki: proje sahibi tanıtım deposunun eylemedotdev olarak adlandırılmasını, tüm içerik ve görsellerin Eyleme ile hizalanmasını doğrudan istedi; ardından eyleme.dev adresini seçti. eylema.dev adresini kapattığını ve eyleme.dev adresini henüz satın almadığını doğruladı. Yeni kimlik hazırlanır; alan adı satın alma, DNS değişikliği ve dağıtım yapılmaz. Mevcut arama dışı bırakma politikası ve tarihsel kanıtlar korunur.

Depo adı: GitHub, özgün depoyla aynı 1414388661 kimliğini eyleme-dev/eylemedotdev adıyla, herkese açık ve varsayılan main dalıyla döndürdü. Yerel origin yeni adresi kullanır.

İzinli yollar: etkin README/belgeler, derleme/sürüm araçları ve regresyon verileri, dağıtımın canonical adresi, üretilmiş sayfalar ve görsel dosya adları/içerikleri, varlık kökeni ve bu iki dilli kayıt. Geçmiş alındılar, istemler, kaynak anlık görüntüleri ve planlar kendi revizyonlarının kanıtı olarak kalır. Azure kaynak ve gizli değişken adları korunur.

Kabul: etkin bağlantılar/canonical/hreflang/sosyal/JSON-LD metni eyleme.dev adresini ve yeni depo adını kullanır; EN/TR afişler Eyleme ve eyleme.dev yazar; etkin HTML ve varlık adreslerinde eski ürün adı bulunmaz; varsayılan dil İngilizcedir; noindex, boş sitemap ve kapalı IndexNow korunur. Sözleşmedeki yerel komutlar, deterministik derleme, çeviri anlamı/özetleri, görsel bütünlüğü ve masaüstü/mobil EN/TR tarayıcı davranışı doğrulanır. Taslak PR açılır. Genel DNS/TLS/dağıtım: not_run; yeni alan adı alınmamıştır.

Bütçeler: tek kapsamlı dal/PR, iki görsel düzenlemesi ve görsel başına en fazla bir hedefli düzeltme, iki yerel onarım döngüsü, dört dil/ekran kontrolü içeren tek tarayıcı oturumu. Riskler: üretilen metnin bozulması, eski görsel yolları ve erken canonical adres dağıtımı. Görsel metinleri ve bağlantılar incelenir; yeni alan adı yayın eşiklerini sağlayana kadar merge/dağıtım yapılmaz.

Roller: Codex; GitHub CLI, Python standart kütüphane araçları, yerleşik Image Gen ve tarayıcı otomasyonu ile mimar, uygulayıcı, doğrulayıcı ve kendi incelemesini yapan kişidir. Bağımsız inceleme bekliyor; ayrı inceleyici iddiası yoktur. Site doğrulaması Rust/GPU/model/eğitim kanıtı değildir.

## Doğrulama kaydı

Bu PR başında (CI tam SHA değerlerini kaydeder), macOS arm64 ve Python 3.15.0 ile geçti: sözleşmedeki venv/hash kilitli kurulum, 43 birim testi, deterministik çıktı, depo denetimi, boş şablon ve boşluk kontrolleri. Özetler yenilenmeden önce EN/TR anlamları incelendi. İki yerleşik Image Gen düzenlemesi hedeflenen alt bilgi alan adını değiştirdi; tam boy PNG dosyaları etiketler, oklar, izin sınırları ve kabul uyarıları bakımından girdilerle görsel olarak karşılaştırıldı. İki 1672 x 941 WebP dosyasının çözülmüş pikselleri PNG eşleriyle tam eşleşiyor; envanter özetleri ve baytları yenilendi. [Tam istemler](website-identity-prompts.json).

Browser eklentisi mevcut değil; Codex uygulama içi tarayıcısının belgelenmiş CUA Playwright arayüzüyle yerel 127.0.0.1 üzerinde 4196 ve 4197 portları, 1280 x 800 ve 390 x 844 boyutlarında sınandı. Varsayılan İngilizce ve iki yönde dil geçişi, sayfa kimliği/dolu içerik/hata katmanı yokluğu, Eyleme logoları, yeni alan adı canonical metaverisi, yüklenen görseller, yatay taşma yokluğu, ok tuşuyla mimari sekmesi seçimi ve doğal soru açılımı geçti. Başarılı site oturumunda konsol uyarısı/hatası yok. İlk önizleme sunucu başlamadan açıldığı için bağlantı reddedildi; sunucu başlatılıp düzeldi. Bellekte kalan eski Türkçe afiş, yeni yerel adreste tekrar kontrol edilerek eyleme.dev gösterdi. Bunlar yerel kontrollerdir; canonical sunucu kanıtı değildir. Bu tur JavaScript kapatma/azaltılmış hareket ayarı: not_run; mevcut yapısal testler ilk HTML içindeki yanıtları hâlâ doğruluyor. Ekran görüntüleri herkese açık deponun dışında tutulur.

Deponun About açıklaması artık Eyleme ve hazırlanan eyleme.dev adresini kullanır; ana sayfa alanı yayına kadar boş kalır. Kendi incelememde kapsamlı diff, güncel HTML/varlık adları, köken, arama politikası ve herkese açık yol/gizli veri kontrolleri denetlendi. Bağımsız inceleme bekliyor. CI bu kayıtta bekliyor. Merge, dağıtım, satın alma, DNS, Azure değişikliği ve indeksleme gönderimleri: not_run; yeni alan adı alınmadı. Tarihsel raporlar ve arama takipleri değişmedi.
