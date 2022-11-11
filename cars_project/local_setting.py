# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b@h$wu)1wu&dpuc0l7ga!zsuxwl6=^y&gz#_g4ph$ktsn$j7h8'




# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}