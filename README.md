# bmstu



## Сначала установить окруржение

python3.10 -m venv venv
source venv/bin/activate

скачиваем зависмости
## pip install -r requirements.txt

проверить, установлена ли MySql на устройстве

сохраняем миграции для бд
python manage.py makemigrations

запускаем миграции для базы данных
python manage.py migrate

запуск сервера для тестов

python manage.py runserver 8001