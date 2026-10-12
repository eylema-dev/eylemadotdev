# IndexNow etkinleştirmesi

[English](indexnow.md). Görev `WEB-005`, revizyon `0.1.0`, 12 Ekim 2026.

Yetki: proje sahibinin mevcut konuşmada `eylema.dev` için IndexNow'u etkinleştirme ve İngilizce/Türkçe sayfaları gönderme isteği ile sitenin umayos aboneliğinde Free `rg-eylema-dev / swa-eylema-dev` hedefine yayınlanması için mevcut izni. DNS, hesap, abonelik veya barındırma planı değişikliği gerekmez.

Taban: güncel `origin/main` üzerindeki `425834d978160f8e0f1b6f5cbc049b3add3e0164`. Dal: `codex/indexnow`. İzinli yollar: `tools/build.py`, `tools/indexnow.py`, `tools/tests/test_indexnow.py`, `public/<IndexNow-key>.txt`, iki keşif rehberi, bu iki dilli kayıt ve `tools/translation-pairs.json`. Sayfa metni ve platform deposu kapsam dışındadır.

Kabul: kökte UTF-8 anahtar dosyası üretmek; deterministik çıktıyı ve olumsuz testleri doğrulamak; dosyayı mevcut yayın envanterine dahil etmek; taslak PR ve mevcut main dağıtımıyla yayınlamak; yayın revizyonunu ve herkese açık anahtarı normal HTTPS üzerinden doğrulamak; yalnızca `https://eylema.dev/` ve `https://eylema.dev/tr/` adreslerini gönderip gerçek HTTP alındısını kaydetmek. HTTP 200 gönderim alındısıdır; 202 anahtar doğrulamasının beklediğini belirtir. Hiçbiri indeksleme kanıtı değildir.

Mimar, uygulayıcı, doğrulayıcı ve öz incelemeci: bu Codex oturumu (belirli model kimliği araçta sunulmuyor). Araçlar: Python standart kitaplığı, Git, GitHub CLI, resmi protokol belgeleri ve mevcut Azure/GitHub yayın kontrolleri. Bağımsız incelemeci iddiası yoktur. Proje sahibinin yetkisi CI ve öz incelemeden ayrıdır.

Riskler: anahtar/dosya uyuşmazlığı, eski dağıtım, kabul edilmemiş gönderim ve gönderimi indeksleme sanmak. Sahiplik anahtarı ve dosyası bilinçli olarak herkese açıktır; hesap veya dağıtım kimlik bilgisi değildir. Komut varsayılan olarak önizleme yapar; yalnızca `--submit` ile tek, sınırlı gönderim gerçekleştirir. İlgisiz dağıtımlarda otomatik yeniden gönderim yapılmaz. Bütçe: 60 dakika, başarısız kontrol başına en fazla üç onarım turu ve gözlenen hata çözüldükten sonra en fazla üç gönderim denemesi; ücretli hizmet yoktur.

Bu PR başında macOS ve Python 3.14.8 ile yerel doğrulama geçti: sanal ortam ve özetle kilitli bağımlılık kurulumu; 31 birim testinin tamamı; depo kontrolleri; boş PR şablonu yapısı; üretilen çıktı güncelliği; diff boşluk kontrolü ve gönderim önizlemesi. Parmak izlerini yenilemeden önce İngilizce/Türkçe rehberler ve görev kayıtları incelendi. Öz incelemede yalnızca kapsam içindeki herkese açık sahiplik dosyası, standart kitaplık araçları ve belgeler bulundu. PR CI, üretim yayını ve gerçek protokol alındısı çalıştırılana kadar beklemededir. Sayfa görünümü ve etkileşimleri değişmediği için UI kontrolleri uygulanamaz. Yetkili indeksleme durumu mevcut Google ve Bing izleyicilerinin sorumluluğundadır.
