# bmstu

## Инструкция по установке 

### Сначала установить окруржение

```
python3.10 -m venv venv
source venv/bin/activate
```

### скачиваем зависмости

```
pip install -r requirements.txt

```
проверить, установлена ли MySql на устройстве

сохраняем миграции для бд

```
python manage.py makemigrations
```

запускаем миграции для базы данных

```
python manage.py migrate
```

запуск сервера для тестов

```
python manage.py runserver 8001



## Cоздать суперпользователя

Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.


## Панель админисьратора достпна по ссылке
http://127.0.0.1:8001/admin/

