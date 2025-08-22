# user_service_backup

## Amaç
Bu proje, yedekleme (backup) kavramını öğretmek ve uygulamalı olarak göstermek için hazırlanmıştır. Kullanıcı verileri basit bir JSON dosyasında tutulur ve istenildiğinde yedeklenip geri yüklenebilir.

## Backup (Yedekleme) Nedir?
Backup, önemli verilerin kaybolmasını önlemek için bir kopyasının alınmasıdır. Bu projede, kullanıcı verileri `users.json` dosyasında tutulur ve yedekleme işlemiyle bu veriler `backup.json` dosyasına kopyalanır. Ayrıca, yedek dosyası her yedeklemede otomatik olarak GitHub'a gönderilir.

## Özellikler
- Kullanıcı ekleme
- Kullanıcı verilerini yedekleme (backup)
- Yedekten geri yükleme (restore)
- Yedek dosyasını otomatik olarak GitHub'a gönderme

## Kullanım
1. Kullanıcı ekle
2. Yedekle (backup)
3. Yedekten geri yükle (restore)

## Nasıl Çalışır?
- Yedekleme işlemi sırasında, `backup.json` dosyası güncellenir ve otomatik olarak GitHub'a commit & push edilir.
- Geri yükleme işlemi, yerel `backup.json` dosyasından yapılır. En güncel yedeği almak için önce `git pull` komutunu kullanabilirsin.

## Başlatmak için
```bash
python main.py
```

---
Bu proje, yedekleme mantığını uygulamalı olarak göstermek için hazırlanmıştır.
