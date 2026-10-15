# Türkçe eyleme geçiş ifadesi

WEB-019 revizyon 0.1.0, 15 Ekim 2026. Main tabanı 9470abae7221cde5de512d38ba1eda5ef8ad1d28; dal codex/turkish-action-copy. Yetki: proje sahibi, yetkilendirilmiş site yayını sırasında Türkçede "eyleme geçmek" ifadesinin kullanılmasını istedi.

Plan ve izinli yollar: content/tr.json içindeki ana başlık "Niyetten / eyleme. / Tasarımla." yerine "Niyetten / eyleme geç. / Tasarımla." olur; public/tr/index.html yeniden üretilir, bu iki dilli kayıt ve tools/translation-pairs.json güncellenir. İngilizce "From intent / to action. / By design." aynı anlamı taşıdığı için değişmez. Mimari, görseller, arama politikası, izinler ve bağımlılıklar değişmez.

Kabul: mevcut 43 test ve depo/üretim/PR/fark eşikleri; parmak izlerinden önce EN/TR anlam incelemesi; masaüstü ve 390px mobil görünümde satır kırılması/taşma incelemesi; dağıtım sonrası tam merge SHA ile canonical canlı özet/MIME/noindex/404 doğrulaması. Geri alınabilir metin değişikliğini aynalayan yeni test eklenmez. Site kontrolleri platform çalıştırma kanıtı değildir.

Bütçe: tek kapsamlı PR/merge/dağıtım, en fazla iki onarım döngüsü. Risk: uzayan Türkçe satır kırılabilir; okunabilir tam metin korunur. Gerekirse kapsamlı metin commit'i geri alınır. Roller: Codex, GitHub CLI, Python ve belgelenmiş CUA ile mimar, uygulayıcı, doğrulayıcı ve kendi inceleyicisidir; bağımsız inceleyici iddiası yoktur. Yerel, CI, tarayıcı ve yayın eşikleri PR'da ayrı kaydedilir.
