"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os

from configurations import Configuration
from configurations.values import SecretValue

__author__ = "Mihail Butnaru"
__copyright__ = "Copyright 2020, All rights reserved."

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = "=hp0a+m%bzc13e*9x73q%21nm+$drt$6!3fbbbxmhv(6rbp&)z"

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = [
        "crypto",
        "rest_framework",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "core.urls"

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
                ],
            },
        },
    ]

    WSGI_APPLICATION = "core.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    STATIC_URL = "/static/"

    REST_FRAMEWORK = {
        "EXCEPTION_HANDLER": "crypto.exceptions.exception_handler.custom_exception_handler"
    }

    # Twitter AUTH Credentials
    TWITTER_CONSUMER_KEY = SecretValue(
        environ_name="TWITTER_CONSUMER_KEY", environ_prefix=None
    )
    TWITTER_CONSUMER_SECRET = SecretValue(
        environ_name="TWITTER_CONSUMER_SECRET", environ_prefix=None
    )
    TWITTER_ACCESS_TOKEN = SecretValue(
        environ_name="TWITTER_ACCESS_TOKEN", environ_prefix=None
    )
    TWITTER_ACCESS_TOKEN_SECRET = SecretValue(
        environ_name="TWITTER_ACCESS_TOKEN_SECRET", environ_prefix=None
    )

    NUMBER_OF_TWEETS = 500
