# Azure site yayını

12 Ekim 2026 ek düzeltmesi: üretilen Azure alan adı, varlık yolları dahil canonical eylema.dev adresine HTTP 301 yönlendirmesi yapıyor. Üretim iş akışı; commit, dosya envanteri, hash, MIME, varlık yönlendirmesizliği ve gerçek 404 kontrollerini koruyarak doğrudan canonical adresi doğrular. Sürüm yayılımı için on saniye arayla en çok üç tam doğrulama denemesi yapılır; hiçbiri geçmezse akış yine başarısız olur. Bu düzeltme DNS, Azure kaynağı veya izin değişikliği içermez.

[English](deployment.md). Görev `WEB-002 / 0.1.0`, 11 Ekim 2026.

Yetki: proje sahibi PR #1'in birleştirilmesini ve `eylema.dev` sitesinin `umayos subscription`, `rg-eylema-dev`, `swa-eylema-dev`, Free katmanıyla yayınlanmasını açıkça istedi. Bu, genel portföy becerisindeki adlandırma/abonelik/özel alan adı kullanmama varsayımlarının yerini alır. Alan adı sağlayıcısı GoDaddy olarak belirtildi. Ücretli katman, DNS sağlayıcısı taşıma veya ilgisiz kaynak değişikliği yetkili değildir.

Taban: PR #1'in yetkili squash birleşmesi sonrası main `1dc595e166e3a84b687d42370a84a8a55b78d0d5`. Dal: `codex/azure-eylema-release`. İzin verilen yollar: dağıtım iş akışı, public sunucu yapılandırması, sürüm/canlı kontrol araçları ve regresyon testleri, iki dilli yayın/katkı belgeleri ve çeviri özetleri. Site tasarımı ve ilgisiz platform çalışmaları korunur.

Hedef: `eylema-dev/eylemadotdev`, main, West Europe, Free, `rg-eylema-dev / swa-eylema-dev`. Canlı abonelik Enabled durumunda; bu yayından önce iki Free uygulaması vardı. Çıktı: `public/`; iş akışı: `.github/workflows/deploy-swa-eylema-dev.yml`; gizli değişken: `AZURE_STATIC_WEB_APPS_API_TOKEN_SWA_EYLEMA_DEV`; eşzamanlılık grubu: `production-swa-eylema-dev`. Yalnızca bu dağıtım anahtarı Azure'dan GitHub'a doğrudan, yazdırılmadan veya saklanmadan aktarılır.

Kabul: AGENTS komutları ve olumsuz sürüm/yapılandırma testleri; doğrulama, hazır çıktı yükleme ve canlı HTTP denetimi yapan tek üretim akışı; Git/Actions/sürüm SHA eşleşmesi; Azure Free/Ready; üretilen alan adı ve eylema.dev HTTPS, kaynak özeti/MIME, gerçek 404, canonical dil yolları, masaüstü/mobil tarayıcı ve logo kontrolleri. DNS kaydı, genel yayılım ve sertifika hazırlığı ayrı kanıtlardır. İndeksleme ve saha Core Web Vitals ölçülmüş değildir.

Riskler: çift dağıtım akışı, yanlış abonelik, eski sürüm, yanlış SPA fallback, bozulan statik varlıklar, kök DNS sınırları/yayılımı. Açık abonelik kimliği, otomatik kaynak iş akışı olmaması, sıralı dağıtım, trailingSlash auto, gerçek 404 ve dosya özetleri kullanılır. İlgisiz DNS/e-posta kayıtları korunur, yönlendirme kayıtları değişmeden önce incelenir.

Bütçe: uygulama/doğrulama 90 dakika; başarısız kontrol başına en çok üç odaklı düzeltme; anlamlı güncellemelerle sınırlı DNS yoklaması. Mimar, uygulayıcı, doğrulayıcı ve öz incelemeci aynı Codex GPT-6 ailesi oturumudur; bağımsız inceleme uydurulmaz. Yayın/birleştirme proje sahibince açıkça yetkilidir. Araçlar: Git/GitHub CLI, Azure CLI, Python standart kütüphanesi, CUA tarayıcı/yerel Chrome ve resmi Microsoft/Azure belgeleri.

Kök alan adı için [Microsoft dış DNS rehberi](https://learn.microsoft.com/en-us/azure/static-web-apps/apex-domain-external) izlenir. Varsa ALIAS/ANAME/flattening tercih edilir; GoDaddy yalnızca A kaydı sunarsa tam uygulamanın stableInboundIP değeri kullanılır ve bölgesel yönlendirme sınırı kaydedilir. Kök alana standart CNAME konmaz. Sunucu ayarları [Azure yapılandırmasını](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration) izler.
