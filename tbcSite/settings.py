"""
Django settings for tbcSite project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
from django.db import connections

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SPATIALITE_LIBRARY_PATH='/usr/local/lib/mod_spatialite.dylib'

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p^ld9gqkhlc-gzm(c=w(a!jzpm)p4d*_=h(&emgvt6p+%3taj%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.gis',
	'rest_framework',
	'rest_framework.authtoken',
	'main',
	'usuarios',
	'vcubs',
	'movibuses',
	'tranvias'
)

# Middleware classes
MIDDLEWARE_CLASSES = ()

# Root urls file
ROOT_URLCONF = 'tbcSite.urls'

# Templates configuration
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

# Rest Framework
REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
		'rest_framework.permissions.DjangoModelPermissions'
	)
}

WSGI_APPLICATION = 'tbcSite.wsgi.application'

# Database
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'mydb',
		'USER': 'admin',
		'PASSWORD': '123',
		'HOST': '0.0.0.0',
		'PORT': '6432'
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static url path
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

# HTTPS configuration
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 1
SECURE_HSTS_INCLUDE_SUBDOMAINS = True