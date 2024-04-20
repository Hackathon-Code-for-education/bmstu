host="localhost"
user="root"
password="rootegor"



DATABASE_NAME = "AskME" # Or path to database file if using sqlite3.
DATABASE_USER = user # Not used with sqlite3.
DATABASE_PASSWORD = password # Not used with sqlite3.

SECRET_KEY = 'django-insecure-iz_=#7m$w#_37w3(g76p#)lh8*dmm(n97+5le=pbcp0ihtpky^'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
    }
}
