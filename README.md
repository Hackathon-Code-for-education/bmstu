# bmstu

## Презентационные материалы

ЪУЪ.pdf или ЪУЪ.pptx - презентация
ЪУЪ.mp4 - Видео демонстрация

## Инструкция по установке


### Docker

#### Запуск контейнеров

```
docker-compose up
```

#### Миграция базы данных

```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

### Linux

Перед установкой нужно подготовить как минимум 15 гб свободного места на диске.

#### Установка необходимых пакетов

```
sudo apt install git python3-venv 
sudo apt-get install mysql-client mysql-server mariadb-client libmariadb3 libmariadb-dev python3-dev gcc
```

#### Склонировать git

Вместо path произвольная директория

```
cd path
git clone https://github.com/Hackathon-Code-for-education/bmstu.git
cd bmstu
```

#### Установка окруржения

```
python3.10 -m venv venv
source venv/bin/activate
```

#### Cкачивание и установка зависмостей

```
pip install -r requirements.txt
```

#### Сохранение миграций для бд

```
python manage.py makemigrations
```

#### Cоздать пользователя MySql и добавить базу данных 

Настройка mysql. По умолчанию, должен быть юзер "root". Если у вас иначе, ищете способ войти в mysql

Вместо user, password, database замените на собственные данные

```
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
CREATE DATABASE database;
EXIT;
```

#### Настроить базу данных

Необходимо передать данные о бд в программу. Открыть файл [local_settings.py](local_settings.py) и записать данные о mysql в следующую конструкцию:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'имя базы данных',
        'USER': 'имя пользователя mysql',
        'PASSWORD': 'пароль',
    }
}
``` 

#### Запуск миграции для базы данных

```
python manage.py migrate
```

#### Cоздать суперпользователя

```
python manage.py createsuperuser
```

```
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```

#### Запуск сервера для тестов. 

По умолчанию, следующая команда запустит сервер на порте 8000.

```
python manage.py runserver
```

Если у вас этот порт занят, то используете следующую команду. Вместо port вставляете свой.

```
python manage.py runserver port
```

## Функционал

#### Панель администратора достпна по ссылке
http://127.0.0.1:8001/admin/

вручную можно добавить вуз и пользователей

