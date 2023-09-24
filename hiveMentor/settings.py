from pathlib import Path
import os
from environ import Env
from userApp.keys import *

env = Env()
env.read_env()

# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = 'django-insecure-v_ry!op)yp3_cgvw&u2=%biwi4s^uk6znfs4i@4h%hv1ih0t88'
SECRET_KEY = 'KEY'

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['hivementor.beedev-services.com', 'dev.beemindful-buzz.com', 'beemindful-buzz.com']


CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:5500',
    'http://localhost:5173',
    'https://hivementor.beedev-services.com',
    'http://hivementor.beedev.services.com',
    'https://hivechat.beedev.services.com',
    'http://hivechat.beedev.services.com',
    'https://dev.thehive-services.com',
    'http://dev.thehive-services.com',
    'http://dev.beemindful-buzz.com',
    'https://dev.beemindful-buzz.com',
    'http://beemindful-buzz.com',
    'https://beemindful-buzz.com',
    'http://chat.beemindful-buzz.com',
    'https://chat.beemindful-buzz.com',
    # Add more allowed origins as necessary
]

CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coreApp.apps.CoreappConfig',
    'userApp.apps.UserappConfig',
    'chatApp.apps.ChatappConfig',
    'logApp.apps.LogappConfig',
    'corsheaders',
    'rest_framework',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.humanize.middleware.HumanizeMiddleware',
]

ROOT_URLCONF = 'hiveMentor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hiveMentor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'craftsnh_hiveMentor',
#         'USER': 'root',
#         'PASSWORD': 'HoneyBee#4',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        # 'ENGINE':'django.db.backends.mysql',
        'NAME': 'thehives_hiveMentor',
        'USER': 'root',
        # 'USER': 'thehives_mentor',
        'PASSWORD': 'HoneyBee#4',
        # 'PASSWORD': 'MrTucker@22',
        'HOST': 'localhost',
        'PORT': '3306',
        # 'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST = 'mail.beedev-services.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_PORT = 465
EMAIL_HOST_USER = 'beedev.services@gmail.com'
EMAIL_HOST_PASSWORD = HOST_PASSWORD
EMAIL_HOST_ALT_USER = 'melissa@beemindful-buzz.com'