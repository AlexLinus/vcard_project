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


# EMAIL SECTION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = '<email_host>'
EMAIL_HOST_USER = '<email>'
EMAIL_HOST_PASSWORD = "<password>"
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_EMAIL_TO = '<email>'