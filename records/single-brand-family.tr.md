# Tek Eyleme markası ve topluluk ürün ailesi

[English](single-brand-family.md). Görev WEB-021, revizyon 0.1.0, 15 Ekim 2026.

## Yetki ve plan

Proje sahibi, depolarda ve eyleme.dev üzerinde tek Eyleme markasını uygulamayı açıkça yetkilendirdi: Eyleme açık kaynak ve topluluk odaklı kalır; Derleme ile Onama kapalı kaynak, ücretli abonelik modeli kullanır. Taban main: 0fa7374a16450afa0015e5c7851816e843f56a6f; dal: codex/eyleme-commercial-family. Ayrı worktree özgün çalışma kopyasını korur. Site uygulayıcısı yalnızca site kaynağından sorumludur; koordinatör ajan depo görünürlüğünü, incelemeyi, birleştirmeyi ve zaten yetkilendirilmiş canonical yayını yönetir.

Kapsam: iki dilli içerik, ortak üretici ve CSS, üretilen İngilizce/Türkçe sayfalar, odaklı regresyon kontrolleri/testleri, README ve katkı eşleri, bu görev kaydı ve çeviri özetleri. Canonical eyleme.dev, indekslenebilir giriş sayfaları, gerçek noindex 404, arama sahiplik dosyaları, devre dışı IndexNow, görsel baytları, dağıtım kimliği ve ayrı tarihsel eylema.dev kaldırma ilkesi korunur. Hesap, ödeme entegrasyonu, fiyat, satış iletişimi, çalışan abonelik hizmeti veya müşteri kanıtı uydurulmaz.

Plan: açık kaynak topluluk aracını girişe taşı, gerçek kurulum/belge/katkı/sorun bağlantıları sun ve Derleme → Onama → Eyleme sıralı herkese açık ürün bölümü ekle. Ticari geliştirme/erişim sınırlarını belirt; çekirdek yetkilendirmeyi ücretli ürünlerden bağımsız tut. İngilizce/Türkçe anlamı ve mevcut görselleri incele, sayfaları yeniden üret, yerel kontrolleri çalıştır, masaüstü/mobil davranışı incele ve taslak PR teslim et. Mevcut mimari görseli açık kaynak aracı anlatır; kapsam bildirimi ücretli hizmetlerin zaten bütünleştiğini ima etmeden açık kalır.

## Kabul ve kaynaklar

Ortak adlandırma, bağımsız Apache-2.0 çekirdek kullanımı, kapalı kaynak abonelik tanımları, private ürün depolarına açık bağlantı ve ödeme akışı olmaması, çalışma zamanı/pilot sınırlarının korunması kabul ölçütleridir. Üretilen çıktı, çeviri yapısı/özetleri, gizlilik/bağlantı regresyonları, tam depo kontrolleri, doldurulmuş gerçek PR metni ve tarayıcı etkileşimleri doğrulanır. PR CI ve canonical üretim yayını, incelemeden sonra koordineli yürütülen ayrı eşiklerdir.

Bütçe: 60 dakika; başarısız kontrol başına en fazla üç odaklı onarım; yeni üretim bağımlılığı veya görsel üretimi yok. Risk: ücretsiz çekirdek yetkisini ücretli Onama ile karıştırmak veya pilot kapsamını üretimde abonelik gibi sunmak. Görünür metin ve regresyon kontrolleri bu ayrımları korur. Geri dönüş bu kapsamlı commit’in geri alınmasıdır; çalışma zamanı, hesap veya ödeme geçişi yapılmaz.

## Roller ve doğrulama

Nitelikli mimari: proje sahibince onaylı, 13 Kasım 2026 tarihine kadar geçerli sol61-high-contracts-2026-10-14 profili altında ayrı yapılandırılmış gpt-6.1-sol / high bağlamı, depolar arası marka, lisans ve kabul tasarımını sağladı. Site uygulayıcısı/doğrulayıcısı/öz inceleyicisi: Git/GitHub CLI, Python standart kitaplığı ve belgelenmiş CUA uygulama içi tarayıcısını kullanan görevlendirilmiş Codex site ajanı. Koordinatör gpt-6-astra / ultra bağlamı ek uygulama/doğrulama desteğidir; kabul edilmiş mimar profili değildir. Gizli sunum kimliği bilinmiyor. Son revizyonların farklı nitelikli bağımsız bağlamda incelemesi bekliyor. Öz inceleme bağımsız inceleme değildir.

Yerel kontrol noktası: geçti — özet kilitli bağımlılık kurulumu, ürün ailesi/gizlilik için dört odaklı regresyon dahil 48 Python testi ve belirlenimci üretim. Çeviri özetleri yenilenmeden önce İngilizce/Türkçe anlam incelendi. Mevcut İngilizce ve Türkçe mimari görselleri görsel olarak incelendi: yalnızca Eyleme adını içerir, planlanan eğitim/bütünleşik kabulü ayırır, ücretli ürün veya fiyat iddiası taşımaz. Tüm görsel baytları değişmeden kaldı. Son depo/özet/PR kontrolleri, tarayıcı ve uzak CI kanıtı çalıştırıldığında aşağıya kaydedilir. Bu site çalışmasında Rust, çıkarım, GPU, eğitim veya ticari hizmet yürütmesi test edilmedi.

Tarayıcı kontrol noktası: geçti — CUA uygulama içi tarayıcıda masaüstü 1280 × 800 ve mobil 390 × 844, iki dil rotası, ürün/topluluk bağlantıları, ürün sırası, kurulum/katkı hedefleri, Assign → ArrowRight → Inspect ve yeni abonelik açıklaması. Yatay taşma veya yakalanan konsol uyarısı/hatası yok. İlk Chrome giriş noktası erişilemedi; alt ajanda görünür IAB desteklenmedi; arka plandaki IAB başarılı oldu. Summary öğesi için button rolü yerine metin seçicisi gerekti; bu ürün hatası değil test seçicisi düzeltmesiydi. İngilizce giriş başlığı görsel incelemeden sonra “Together.” olarak kısaltıldı. Herkese açık GitHub Issues ve Discussions açık (salt okunur API ile doğrulandı); topluluk çağrıları açık Discussions sayfasını kullanır. Son metin sonrası tarayıcı doğrulaması aşağıya eklenecektir.

Son yerel kontrol noktası: geçti — üretim/güncellik kontrolü, depo ve incelenmiş çeviri özeti, boş şablon yapısı, doldurulmuş PR metni doğrulaması, boşluk kontrolü ve 48 testin tamamı. Son İngilizce mobil giriş ve masaüstü ürün bölümü görsel olarak geçti; Türkçe mobil topluluk ve açıklama geçti. Yakalanan sayfa hatası/uyarısı yok; gözlenen görsel yükleme hatası yok. Görünüm boyutu geçersiz kılması sıfırlandı. İki tarayıcı seçicisi düzeltildi (summary rolü ve desteklenmeyen başlık düzeyi seçeneği); sonrasında desteklenen seçicilerle kontroller başarılı oldu. Bu commit aşamasında CI, gerçek ayrı son inceleme, birleştirme ve üretim yayını bekliyor.
