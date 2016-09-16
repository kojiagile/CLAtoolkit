"""
Django settings for clatoolkit_project project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR, "../.env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("DEBUG") == '1':
    DEBUG = True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

ADMINS = os.environ.get("ADMINS").split(",")
ADMINS = map(lambda email: email.split(":"), ADMINS)

if ADMINS:

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    SERVER_EMAIL = os.environ.get("SERVER_EMAIL")

    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = os.environ.get("EMAIL_PORT")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

    if os.environ.get("EMAIL_USE_TLS") == '1':
        EMAIL_USE_TLS = True

    if os.environ.get("EMAIL_USE_SSL") == '1':
        EMAIL_USE_SSL = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'clatoolkit',
    'dataintegration',
    'dashboard'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'clatoolkit_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'clatoolkit_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }

}'''

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : os.environ.get("DB_NAME"),
        'USER' : os.environ.get("DB_USER"),
        'PASSWORD' : os.environ.get("DB_PASS"),
        'HOST' : os.environ.get("DB_HOST"),
        'PORT' : os.environ.get("DB_PORT")
    },
    
    'tweetimport': {
	'ENGINE': 'django.db.backends.sqlite3',
	'NAME': os.path.join(BASE_DIR, 'tweetimport.sqlite3'),
    }
}

REST_FRAMEWORK = {
	'UNAUTHENTICATED_USER': None,
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# web accessible folder
STATIC_ROOT = BASE_DIR #os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR,'static')

# Additional locations of static files
STATICFILES_DIRS = (
    # location of your application, should not be public web accessible
    STATIC_PATH,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

AUTH_PROFILE_MODULE = "account.userprofile"

GA_TRACKING_ID = ''
#
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
#MEDIA_URL = '/static/'

#####################################################
######### Load Social Media Data Integration plugins
#####################################################

import sys
import pkgutil
DI_PATH = os.path.join(BASE_DIR,'dataintegration')
sys.path.append(DI_PATH)
PLUGIN_PATH = os.path.join(DI_PATH,'plugins')
pluginModules = [name for _, name, _ in pkgutil.iter_modules([PLUGIN_PATH])]
from dataintegration.core.plugins.loader import load_dataintegration_plugins
from dataintegration.core.plugins.registry import get_includeindashboardwidgets, get_plugins, get_includeindashboardwidgets_verbs, get_includeindashboardwidgets_platforms, get_includeauthomaticplugins_platforms
load_dataintegration_plugins(pluginModules)

DATAINTEGRATION_PLUGINS_INCLUDEDASHBOARD_VERBS = get_includeindashboardwidgets_verbs()
DATAINTEGRATION_PLUGINS_INCLUDEDASHBOARD_PLATFORMS = get_includeindashboardwidgets_platforms()
DATAINTEGRATION_PLUGINS = get_plugins()
DATAINTEGRATION_PLUGINS_INCLUDEAUTHOMATIC = get_includeauthomaticplugins_platforms()
