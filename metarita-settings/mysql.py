import os
from .base import *

SECRET_KEY = 'd3j@zo1psh*&-u35#ayi'

INSTALLED_APPS += ('teimporter',)

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'teihencer-play',
        'USER': 'teihencer',
        'PASSWORD': 'BHziF6wsdU*q',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


ROOT_URLCONF = 'custom_urls.urls'
