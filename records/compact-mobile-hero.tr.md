# Kompakt mobil giriş

[English](compact-mobile-hero.md). Görev WEB-025, sürüm 0.1.0, 15 Ekim 2026.

Yetki: bakım sorumlusu üçgenin mobilde sloganın hemen altına taşınmasını, girişin daha kompakt olmasını, iki dilde kontrol edilmesini ve yayımlanmasını doğrudan istedi. Taban: güncel `origin/main` olan `e38f04d1fd0c7d9a6ae9add4a0bbb21abc0b68cf`. Dal: mevcut yalıtılmış site çalışma ağacındaki `codex/compact-mobile-hero`.

Plan: ortak giriş bölümünün belge sırasını başlık → görsel → açıklama yapıp duyarlı ızgara alanları tanımlamak; masaüstündeki iki sütunlu düzeni korumak; metin veya görsel açıklaması kaldırmadan mobil boşlukları, başlık boyutunu ve paragraf aralıklarını sıkılaştırmak. İzinli yollar: `tools/build.py`, `public/assets/site.css`, üretilen `public/index.html` ve `public/tr/index.html`, bu iki dilli kayıt ve `tools/translation-pairs.json`.

Kabul: mobil genişliklerde görünen üçgen sloganı takip edip açıklamadan önce gelir, girişin toplam yüksekliği önceki yayından kısadır, içerik çakışmaz veya taşmaz. İki tam sloganı, açıklamalı bilgilendirici görseli, masaüstü düzenini, dil geçişini, klavye gezinmesini ve açılır yanıtları doğrulamak. Katkıcı komutlarının tamamını, belirlenimci çıktı ve doldurulmuş PR kontrollerini çalıştırmak; göndermeden önce bütün farkı öz incelemeden geçirmek. PR'nin tam sürümündeki kontroller ve inceleme konuları denetlendikten sonra main kontrollerini, Azure durumunu, kanonik HTTPS sürüm/dosya özeti kontrollerini ve iki canlı dili doğrulayıp dalı temizlemek.

Bütçe: 30 dakika, başarısız kapı başına en çok üç odaklı onarım, yeni bağımlılık veya ücretli kaynak yok. Riskler: ızgara satırı boyutları, masaüstü görünümünün kayması ve dar ekranda üçgenin okunabilirliği. Tarayıcı geometrisi, ekran görüntüleri ve etkileşimler yerleşim kanıtı sağlar; statik kontroller tek başına yeterli değildir. Geri dönüş: sınırlı yerleşim değişikliğini geri alıp yeniden yayımlamak.

Mimar, uygulayıcı, doğrulayıcı ve öz inceleyici: Python, Git/GitHub CLI, Azure CLI ve mevcut paketli Playwright/Chromium kullanan bu Codex GPT-6 oturumu. Browser eklentisi mevcut değil. Bağımsız inceleyici iddiası yoktur. İngilizce/Türkçe metinlerin anlamı değişmez; üretilen iki sayfa ve bu eş kayıt incelenir. Kanıtlar PR ve teslim raporuna kaydedilir. Ürün çalışma zamanı, ticari hizmet ve saha kabulü uygulanmaz.
