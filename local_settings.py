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


"""

host="37.46.128.88"
#LocalDataSource: @37.46.128.88
#BEGIN#

user="test"
password="nicqeb-wotWi8-bybmym"

DATABASE_NAME = "askme" # Or path to database file if using sqlite3.
DATABASE_USER = user # Not used with sqlite3.
DATABASE_PASSWORD = password # Not used with sqlite3.

SECRET_KEY = 'django-insecure-lo^nkte)dr3ass6h*tq52*jsb^jj&_&s4+ih_r6(nz=2o42t@7'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': host,
        'PORT': '3306',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
    }
}

"""



"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': DATABASE_NAME,
        'USER': 'test',
        'PASSWORD': 'nicqeb-wotWi8-bybmym',
    }
}
"""


"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': DATABASE_NAME,
        'USER': 'test',
        'PASSWORD': 'nicqeb-wotWi8-bybmym',
    }
}
"""