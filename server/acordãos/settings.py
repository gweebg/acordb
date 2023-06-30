"""
Django settings for acordãos project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from pymongo import MongoClient
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9ciqs71-bhdsf_tnc^+f@r-oe0w$gzt$-^lfge21ceb*2_9_wu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','localhost','127.0.0.1', 'api-server','*','172.26.113.96', 'eivarin.xyz']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    'rest_framework',
    'rest_framework_api_key',
    "rest_framework_swagger",
    'drf_yasg',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    'corsheaders',
    'drf_spectacular',
    
    'accounts',
    'records',
    'favorites'
]
AUTH_USER_MODEL='accounts.Account'

AUTHENTICATION_BACKENDS = (
    'accounts.authentication.APIKeyAuthenticationBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.github.GithubOAuth2',
    
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'accounts.authentication.APIKeyAuthenticationBackend',
       'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  
       'drf_social_oauth2.authentication.SocialAuthentication',
   ),
   
   'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Acordb Server'
}
OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 26784000,
}

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = [
#    "http://localhost:8000",
#    "http://127.0.0.1:8000"
# ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = "acordãos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = "acordãos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'acordaos',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'postgres',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Europe/Lisbon'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

SOCIAL_AUTH_URL_NAMESPACE = 'accounts:social'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '172096125699052'
SOCIAL_AUTH_FACEBOOK_SECRET = '4129a410c152648a9775efa402f9eb98'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
   'fields': 'id, name, email'
}
SOCIAL_AUTH_USER_FIELDS=['email','first_name','username','password']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "316555827922-thlb7qjblpqovk9033h29ub4rejimaqd.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

SOCIAL_AUTH_GITHUB_KEY = 'c048c9348cc4806b54f6'
SOCIAL_AUTH_GITHUB_SECRET = 'f441631759055d5b2eec7871bd9b14457d3d7780'

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
   'https://www.googleapis.com/auth/userinfo.email',
   'https://www.googleapis.com/auth/userinfo.profile',
]

DEFAULT_CLIENT_ID="TIB1j6dKXtEQoB3kAp8dXTsYlBkUfG3GkLmO1Oph"
DEFAULT_CLIENT_SECRET="qlBGPrFBzH05tJxciMzfPCVRIrdFacDXS3GAacCixyQWBLfOB6LP4iMSEr77nu7s80X84KCQZuxT6h4Z0Qa7WCjLJFcCOho37STViWVo1vA55tOoYqdb2vznQtl0ZN7d"

MONGO_DB = MongoClient('mongodb://mongodb:27017/',socketTimeoutMS=500000)['acordaos']
MONGO_DB['records'].create_index([('id_acordao', 1), ('record_added_at', -1)])
MONGO_DB['records'].create_index([('record_added_at', -1)])
DATA_UPLOAD_MAX_NUMBER_FIELDS=1000000