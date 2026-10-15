# Web sitesine katkı

[English](CONTRIBUTING.md). [AGENTS.md](AGENTS.md) ve [kalite kontrollerini](docs/tr/quality-gates.md) izleyin.

Bu, proje sahibinin yetkilendirdiği ayrı ve herkese açık tanıtım sitesi deposudur. Açık platform tasarımı [eyleme-dev/eyleme](https://github.com/eyleme-dev/eyleme) deposundadır. Bu web sitesi deposu için açık kaynak lisansı seçilmemiştir; açık kaynak Apache-2.0 ifadesi birinci taraf Eyleme çekirdek kod ve belgeleri içindir. Tek Eyleme markasını ve bağımsız topluluk aracını görünür tutun. Derleme ve Onama’yı geliştirme aşamasındaki kapalı kaynak abonelik ürünleri olarak sunun; herkese açık site bağlantıları ziyaretçileri private depolara göndermemelidir. Gerçek kanıt ve yetki olmadan fiyat, ödeme akışı, müşteri yorumu veya üretim hizmeti iddiası eklemeyin.

Güncel main üzerinden tek kapsamlı dal kullanın. İlgili isteği veya sorunu belirtin, sınırlı bir plan kaydedin ve değişiklikleri incelenebilir tutun. Metin kaynakları `content/en.json` ve `content/tr.json` içindedir; ortak HTML/meta verisi `tools/build.py`, sunum `public/assets/site.css` ve `site.js` üzerinden düzenlenir. `.venv/bin/python tools/build.py` ile yeniden üretin.

İki dilin anlamını inceledikten sonra `.venv/bin/python tools/check_repository.py --write-translation-hashes` ve AGENTS.md içindeki tüm komutları çalıştırın. Kontrol aracı olumsuz örnekleri reddetmelidir; değiştirirken anlamlı test ekleyin. Statik kontrolleri tarayıcı, görsel inceleme, CI ve canlı dağıtımdan ayrı raporlayın.

PR şablonunu ve doldurulmuş metin için `.venv/bin/python tools/check_pr.py --body-file <body-file>` komutunu kullanın. Gerçekte kullanılan araç/rolleri belirtin; öz incelemeyi bağımsız incelemeden ayırın ve bekleyen eşikleri bildirin. Özel muhakeme dökümleri, anahtarlar veya işletim kayıtları eklemeyin. İnceleme, birleştirme ve yayınlama kararları proje sahibine aittir. PR kontrolleri salt okunurdur, dağıtım yapmaz. Ayrı yetkili üretim akışı yalnızca kapsamlı Azure anahtarıyla main dalını dağıtır ve canlı sürümü doğrular.
