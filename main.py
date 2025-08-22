# user_service_backup
# Basit kullanıcı servisi ve yedekleme uygulaması

import json
import os

USERS_FILE = 'users.json'
BACKUP_FILE = 'backup.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def backup_users():
    import subprocess
    users = load_users()
    with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)
    print('Yedekleme tamamlandı.')
    # Git işlemleri
    try:
        subprocess.run(['git', 'add', BACKUP_FILE], check=True)
        subprocess.run(['git', 'commit', '-m', 'Backup otomatik yedeklendi'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print('Yedek GitHub\'a gönderildi.')
    except Exception as e:
        print(f'GitHub\'a gönderme sırasında hata oluştu: {e}')

def restore_backup():
    if not os.path.exists(BACKUP_FILE):
        print('Yedek dosyası bulunamadı!')
        return
    with open(BACKUP_FILE, 'r', encoding='utf-8') as f:
        users = json.load(f)
    save_users(users)
    print('Yedekten geri yükleme tamamlandı.')

def add_user(name, email):
    users = load_users()
    user = {'name': name, 'email': email}
    users.append(user)
    save_users(users)
    print(f'Kullanıcı eklendi: {user}')

def main():
    while True:
        print('\n1. Kullanıcı ekle')
        print('2. Yedekle')
        print('3. Yedekten geri yükle')
        print('4. Çıkış')
        secim = input('Seçiminiz: ')
        if secim == '1':
            name = input('İsim: ')
            email = input('Email: ')
            add_user(name, email)
        elif secim == '2':
            backup_users()
        elif secim == '3':
            restore_backup()
        elif secim == '4':
            print('Çıkılıyor...')
            break
        else:
            print('Geçersiz seçim!')

if __name__ == '__main__':
    main()
