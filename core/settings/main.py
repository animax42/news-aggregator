"""
Django settings for techblog project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os,json
from mongoengine import connect

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

try:
    with open('{}/../secrets.json'.format(BASE_DIR)) as json_file:
        SECRETS = json.load(json_file)
except Exception as e:
    SECRETS = {}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = SECRETS.get("DEBUG")

ALLOWED_HOSTS = SECRETS.get("ALLOWED_HOSTS")

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

PROJECT_APPS = ['article']

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR),'article/templates','core/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.media",
                "django.template.context_processors.static"
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

connect('news_aggregator')

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
MEDIA_URL = SECRETS.get("MEDIA_URL")
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

STATIC_URL = SECRETS.get("STATIC_URL")
STATIC_ROOT = os.path.join(MEDIA_ROOT, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [os.path.join(BASE_DIR, '../static_core')]

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
)

COMPRESS_PRECOMPILERS = (
   ('text/scss', 'sass --scss {infile} {outfile}'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

#Storage Config
# DEFAULT_FILE_STORAGE = 'core.custom_storage.StaticStorage'
# STATICFILES_STORAGE = 'core.custom_storage.StaticStorage'
# MEDIAFILES_STORAGE = 'core.custom_storage.MediaStorage'

#Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': SECRETS.get('SYSLOG_ADDR'),
            'formatter':'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['syslog','console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['syslog','console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'info': {
            'handlers': ['syslog'],
            'level': 'INFO'
        },
        'error': {
            'handlers': ['syslog'],
            'level': 'ERROR'
        }
    }
}

