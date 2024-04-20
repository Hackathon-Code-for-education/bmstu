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
```


## Cоздать суперпользователя

```
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```


## Панель администратора достпна по ссылке
http://127.0.0.1:8001/admin/

вручную можно добавить вуз и пользователей


## Cоздать пользователя MySql и добавить базу данных 


## Настроить базу данных

открыть файл [local_settings.py](local_settings.py) и записать 
```
DATABASE_NAME = "Panorama"
user="имя пользователя MySql"
password="пароль"
```

