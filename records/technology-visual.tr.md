# İki dilli teknoloji görseli

Görev WEB-003, revizyon 2, 12 Ekim 2026. [English](technology-visual.md).

Yetki: proje sahibi, son İngilizce açıklayıcı görselin ve Türkçe eşinin eylema.dev üzerinde yayınlanmasını, ayrıca üst soldaki site başlığında görseldeki EylemA yazısının kullanılmasını açıkça istedi. Bu istek, kapsam içindeki PR'ı, mevcut üretim dalına birleştirmeyi ve mevcut iş akışıyla yayını kapsar.

Temel: `878d785242fe75065e255c0fa44630aa4886ff8f`. Dal: `feat/bilingual-technology-visual`.
İzinli yollar: `content/en.json`, `content/tr.json`, `tools/build.py`, üretilen `public/` sayfaları ve site haritası, `public/assets/` görselleri ve CSS, bu iki dilli görev kaydı, varlık kökeni/araç belgeleri ve çeviri parmak izleri. Çalışma zamanı, politika, DNS veya bulut kaynağı değişikliği yoktur.

Revizyon 2 ek düzeltmesi: görsel PR'ı #5, `346035b06ec3eccbd2accce1931ca3b25ffb99c5` olarak birleştirildi; eylema.dev üzerindeki 18 canlı dosya/hash/MIME kontrolü ve iki dilin tarayıcı kontrolleri geçti. İş akışının Azure adresi kontrolü, bu adres eylema.dev'e yönlendiği için başarısız oldu. Kapsamlı onarım bu birleşmeden `fix/canonical-release-verification` dalında başlar; ek izinli alanlar üretim akışının doğrulama hedefi/yeniden deneme bloğu, olumsuz testleri ve iki dilli yayın notlarıdır. Aynı açık yayın yetkisi geçerlidir. Hiçbir doğrulama koşulu kaldırılmaz veya gevşetilmez; üç sınırlı denemenin ardından geçmeyen kontrol başarısız kalır.

Kabul:
- Her dil sayfasında kendi açıklayıcı görseli, açıklayıcı alternatif metni ve tam boy görsel bağlantısı bulunur.
- Sol üst marka, onaylı görselle eşleşir: turuncu E/eylem simgesinin ardından koyu `ylemA`, son A büyük.
- Türkçe posterde aynı marka yazısı ve gözden geçirilmiş Türkçe açıklamalar bulunur.
- Tasarım aşaması açıklaması görünür kalır; yayın, çalışma zamanı/model/GPU kanıtı değildir.
- Katkı sözleşmesindeki tam yerel komutlar ve üretilen çıktı kontrolü geçer. Tarayıcı kontrolleri İngilizce/Türkçe, masaüstü/mobil, dil geçişi, tam boy görsel, mevcut sekmeler ve SSS, konsol ve taşmayı kapsar.
- Yayın; üretim commit'i, başarılı GitHub iş akışı, Azure ortam durumu, canlı sürüm/dosya hash'leri ve eylema.dev tarayıcı davranışıyla doğrulanır.

Riskler: görsel metin doğruluğu, bozuk marka oranları, mobilde okunamayan ayrıntılar ve eski varlıklar. Onaylı PNG kaynak olarak kullanılır; kayıpsız web çıktıları, tam boy bağlantı, doğal en-boy oranları ve sürüm hash'leri kullanılır. Geri dönüş, kapsamlı bir geri alma commit'i ve normal üretim iş akışıdır.

Bütçe: 60 dakika; bir düzeltme dahil en fazla 3 görsel üretim çağrısı; başarısız kontrol başına en fazla 3 hedefli düzeltme; sınırlı CI/bulut sorgulaması. Yeni ücretli kaynak veya çalışma zamanı bağımlılığı yoktur.
Roller: aynı Codex asistanı mimar, uygulayıcı, doğrulayıcı ve öz inceleyicidir. Araçlar: yerleşik Image Gen, Python standart kitaplığı, Git/GitHub CLI, Azure CLI, paketli sharp ve Playwright. Ayrı inceleyici iddiası yoktur. Browser eklentisi becerisi bu oturumda bulunmadığından duyarlı etkileşim doğrulaması paketli Playwright ile yapılır.

Son WEB-003 kaynak ağacında yerel doğrulama geçti: macOS 27.0.1 arm64, Python 3.14.8, Chromium 151.0.7922.34. Tam katkı komutları; 24 mevcut regresyon testi, depo doğrulaması, üretilen çıktı kontrolü, boş şablon doğrulaması ve boşluk denetimi dahil başarılı oldu. Çeviri parmak izleri yenilenmeden İngilizce/Türkçe anlam eşliği gözden geçirildi.

Tarayıcı doğrulaması iki dilde de 1440 × 1000, 390 × 844 ve 320 × 844 boyutlarında geçti: sayfa kimliği, EylemA başlık görseli ve en-boy oranı, dile uygun poster, tam boy PNG sekmesi, dil geçişi, sekmeler ve klavye, SSS ve yatay taşma. JavaScript kapalıyken iki dilde de dört mimari panel görünür kaldı. İlgili konsol uyarısı, sayfa hatası veya başarısız varlık isteği gözlenmedi. Masaüstü, mobil ve görsel bölümü ekran görüntüleri incelendi; başlık seçilen turuncu-E/ylemA görünümüyle eşleşiyor. Ekran görüntüleri ve geçici QA betikleri yayın paketine eklenmez.

Bağımsız inceleme: not_run; yalnızca öz inceleme. Çalışma zamanı/GPU/model/eğitim yürütmesi: bu statik site değişikliği için not_applicable. Yazım anında CI, birleştirme ve canlı yayın bekleniyor; gerçek son commit, iş akışı ve canlı sürüm kanıtı PR'da ve görev tesliminde kaydedilecektir.
