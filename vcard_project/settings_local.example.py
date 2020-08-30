SECRET_KEY = '<secret_key>'

DEBUG = True

ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db_name>',
        'USER': '<db_user>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
