"""
Django settings for mazerango project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z*5cxlhsh8v!7hqpccpn+1n84tz6q&lu@44hq+2q%i&zhq*&m+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost'
]


# Application definition

INSTALLED_APPS = [
    'mazer',
    'mazerango',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mazerango.urls'

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

WSGI_APPLICATION = 'mazerango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# mazerango sidemenu_settings
SIDEMENU_SETTING = [
    {
        'name':
            '사이트 관리',
        'links': [
            {
                'name': '사이트',
                'url': '/admin/company/site',
                'icon': 'fas fa-tv',
                'permissions': ['company.view_site']
            },
            {
                'name': '블랙리스트',
                'url': '/admin/entry/blacklist',
                'icon': 'fas fa-list',
                'permissions': ['entry.view_blacklist'],
            },
        ]
    },
    {
        'name':
            '캠페인 관리',
        'links': [
            {
                'name': '캠페인',
                'url': '/admin/campaign/campaign',
                'icon': 'fas fa-bullhorn',
                'permissions': ['campaign.view_campaign']
            },
        ],
    },
    {
        'name':
            '액션 모듈 관리',
        'links': [
            {
                "name": "액션 모듈 설정",
                "url": "/admin/module/campaignmodule",
                "icon": "fas fa-cogs",
                "permissions": ["campaign.view_campaignmodule"],
            },
            {
                'name': '개인정보',
                'url': '/admin/module/privacy',
                'icon': 'fas fa-user-shield',
                'permissions': ['module.view_privacy']
            },
            {
                'name': '상품',
                'url': '/admin/module/reward',
                'icon': 'fas fa-gift',
                'permissions': ['module.view_reward'],
            },
            {
                'name': '선택형 상품',
                'url': '/admin/module/rewardoptional',
                'icon': 'fas fa-gift',
                'permissions': ['module.view_rewardoptional'],
            },
            {
                'name': '설문',
                'url': '/admin/module/survey',
                'icon': 'fas fa-poll',
                'permissions': ['module.view_survey'],
            },
            {
                'name': '리뷰',
                'url': '/admin/module/review',
                'icon': 'fas fa-comments',
                'permissions': ['module.view_review'],
            },
        ]
    },
    {
        'name':
            '캠페인 참여자 관리',
        'links': [
            {
                'name': '참여자',
                'url': '/admin/entry/entry',
                'icon': 'fas fa-file-alt',
                'permissions': ['entry.view_entry']
            },
            {
                'name': '당첨자',
                'url': '/admin/raffle/winner',
                'icon': 'fas fa-file-alt',
                'permissions': ['raffle.view_winner']
            },
        ]
    },
    {
        'name':
            '운영사 관리',
        'links': [
            {
                'name': '운영사',
                'url': '/admin/company/company',
                'icon': 'fas fa-building',
                'permissions': ['company.view_company']
            },
            {
                'name': '임직원',
                'url': '/admin/company/staffmanage',
                'icon': 'fas fa-user',
                'permissions': ['company.view_staffmanage']
            },
        ]
    },
    {
        'name':
            '사용자 관리',
        'links': [
            {
                'name': '사용자',
                'url': '/admin/siteuser/siteuser',
                'icon': 'fas fa-user',
                'permissions': ['siteuser.view_siteuser']
            },
        ]
    },
]
