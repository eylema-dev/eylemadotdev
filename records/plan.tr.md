# Eylema web sitesi planı

[English](plan.md). Görev `WEB-001`, revizyon `0.2.0`.

Proje sahibinin istekleri (11 Ekim 2026, mevcut Codex görüşmesi): `eylema.dev` tanıtım sitesi, SEO/GEO altyapısı, varsayılan İngilizce ve ayrı kaynak deposu. Son açık istekler depo adını `eylema-dev/eylemadotdev`, görünürlüğünü herkese açık yapar; önceki özel depo tercihinin yerini alır. Depo yayını yetkilidir. Canlı barındırma ve alan adı değişiklikleri ayrı kabul adımıdır.

Taban: `origin/main` üzerindeki site deposu başlangıcı `a08b78d9210035aafdd2db35958f0c2d854c94c2`. Dal: `codex/eylema-website`. İzin verilen yollar: bu ayrı site deposu; platform çalışma dizini düzenlenmez. Site değişiklikleri taslak PR ile sunulur. Yetkili ad değişiminden sonra açık görünürlük ve güncel Git uzak adresi kontrol edilir.

## Kapsam ve kabul

1. Mimari aşamasındaki projeyi mimari 0.3 ve API 0.1 sözleşmelerine dayanarak anlat. Ürün ifadelerini kaynaklarla karşılaştır; planlanan yeteneklerle mevcut belgeleri açıkça ayır.
2. Mevcut Eylema kimliğiyle İngilizce ve Türkçe statik sayfalar üret. Çeviri anahtarlarını, anlam eşdeğerliğini ve oluşturulan dosyaları kontrol et; incelenen içeriklerin özetlerini kaydet.
3. Duyarlı gezinme, dil değişimi, mimari açıklaması ve gerçek kaynak bağlantıları sağla. Masaüstü/mobil, klavye, azaltılmış hareket, JavaScript kapalı temel sayfa ve ana etkileşimleri tarayıcıda dene.
4. Üçüncü taraf site çalışma zamanı paketi, uzak yazı tipi, analitik, hesap akışı veya model servisi ekleme. Tarayıcının HTML/CSS/JavaScript katmanını planlanan birinci taraf Rust platformundan ayrı envanterle.
5. Uygulanabilir depo katkı komutlarını çalıştır, eksik altyapı kontrollerini dürüstçe bildir, yayınlanacak farkı incele ve sağlanan şablonla taslak PR aç. Birleştirme veya dağıtım yapma.

## Tasarım ve kaynaklar

Dört uyumlu konsept: giriş, mimari döngü, kaynaklı sorular/yanıtlar, yol haritası/katkı. Kâğıt `#F7F6F2`, mürekkep `#17252B`, turuncu `#EE5638`; Helvetica Neue/Arial sistem tipografisi, büyük başlıklar, ince çizgiler, açık düzen ve bir üretilmiş heykel görseli. Mevcut logo geometrisi korunur.

Bütçe: uygulama ve doğrulama için 120 dakika, en çok 5 Image Gen çağrısı, başarısız kontrol başına en çok 3 odaklı düzeltme turu. Kontrolü zayıflatmak yerine çözülemeyen hatayı veya eksik gerekli yetkiyi bildir.

## Roller ve riskler

Mimar, uygulayıcı, doğrulayıcı ve öz incelemeci: bu Codex oturumu, GPT-6 ailesi model (tam çalışma zamanı model tanımlayıcısı görünür değil). Gerçekte kullanılan araçlar doğrulama kaydına eklenecek. Ayrı incelemeci iddiası yoktur; bağımsız inceleme ve proje sahibi incelemesi beklemededir.

Başlıca riskler: tasarımı tamamlanmış ürün gibi sunmak, başka çalışmaları taşımak, main dalında olmayan belgelere bağlantı vermek ve site JavaScript'ini planlanan Rust çalışma zamanıyla karıştırmak. Önlemler: kaynaklara dayalı metin, ayrı dal, açık bağımlılık/durum envanteri ve bağlantı kontrolleri. Hesap verisi, gizli anahtar, model ağırlığı veya eğitim kaydı gerekmez.
