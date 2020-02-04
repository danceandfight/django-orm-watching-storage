import os
from dotenv import load_dotenv
from environs import Env
env = Env()
env.read_env()

load_dotenv()

import dj_database_url

DATABASES = {'default': dj_database_url.config(default=env('DATABASE_URL'))}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

#DEBUG = os.getenv('DEBUG')
DEBUG = env.bool('DEBUG') 

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'
