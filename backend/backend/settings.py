"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': int(os.getenv('DB_PORT'))
        }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# メール送信
# ローカル確認用
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 本番環境
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail1002.onamae.ne.jp'
# EMAIL_PORR = 587
# EMAIL_HOST_USER = 'xxx@gmail.com'
# EMAIL_HOST_PASSWORD = 'xxx'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'xxx@gmail.com'

REST_FRAMEWORK = {
    # 認証が必要
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # JWT認証
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    # アクセストークン期限
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    # リフレッシュトークン期限
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
    #認証タイプ
    'AUTH_HEADER_TYPES': ('JWT', ),
    # 認証トークン
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', ),
    'BLACKLIST_AFTER_ROTATION': False,
}

DJOSER = {
    # メールアドレスでログイン
    'LOGIN_FIELD': 'email',
    # アカウント本登録メール
    'SEND_ACTIVATION_EMAIL': True,
    # アカウント本登録完了メール
    'SEND_CONFIRMATION_EMAL': True,
    # メールアドレス変更完了メール
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    # パスワード変更完了メール
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # アカウント登録時に確認用パスワード必須
    'USER_CREATE_PASSWORD_RETYPE': True,
    # メールアドレス変更時に確認用パスワード必須
    'SET_USERNAME_RETYPE': True,
    # パスワード変更時に確認用パスワード必須
    'SET_PASSWORD_RETYPE': True,
    # アカウント本登録用URL
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    # メールアドレスリセット完了用URL
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    # パスワードリセット完了用URL
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    # カスタムユーザー用シリアライザー
    'SERIALIZERS': {
        'user_craete': 'accounts.serializers.UserSerializer',
        'user': 'accounts.serializers.UserSerializer',
        'current_user': 'accounts.serializers.UserSerializer',
    },
    'EMAIL': {
        # アカウント本登録
        'activation': 'accounts.email.ActivationEmail',
        # アカウント本登録完了
        'confirmation': 'accounts.email.ConfirmationEmail',
        # パスワードリセット
        'password_reset': 'accounts.email.PasswordResetEmail',
        # パスワードリセット完了
        'password_changed_confirmation': 'accounts.email.PasswordChangedConfirmaitonEmail',
        # メールアドレスリセット
        'username_reset': 'accounts.email.UsernameResetEmail',
        # メールアドレスリセット完了
        'username_changed_confirmation': 'accounts.email.UsernameChangedConfirmationEmail',
    },
}

AUTH_USER_MODEL = 'accounts.UserAccount'