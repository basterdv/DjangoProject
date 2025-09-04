import os
import logging
from pathlib import Path

from django.conf.urls.static import static
from django.template.context_processors import media

from decouple import config  # Библиотека для управления переменными окружения

logger = logging.getLogger(__name__)  # Инициализируем логер

# Получаем секрет для работы на облаке AMVERA
amvera_var = os.environ.get("AMVERA", '')
secret_key = os.environ.get("SECRET_KEY")

if amvera_var == '1':
    logger.info("AMVERA environment variable set to 1. Работаю в облаке Амвера")
    # SECRET_KEY = secret_key
else:
    logger.info("AMVERA environment variable set to 0. Работаю локально")

# Секретный ключ приложения, считываемый из переменных окружения
SECRET_KEY = config('SECRET_KEY')

# Определяем базовую директорию проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Режим отладки: включается/выключается через переменные окружения
DEBUG = config('DEBUG', default=False, cast=bool)

# Разрешенные хосты для развертывания проекта
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Доверенные источники для CSRF-токенов
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='').split(',')

# Application definition

# Список приложений Django (встроенные)
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Локальные приложения проекта (созданные пользователем)
LOCAL_APPS = [
    'main',
    'goods',
    'users',
    'orders',
]

# Сторонние приложения, установленные через pip
THIRD_PARTY_APPS = [
    'fontawesomefree',
    # "debug_toolbar",
]

# Полный список установленных приложений
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# Список middleware для обработки запросов/ответов
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Корневая конфигурация URL
ROOT_URLCONF = "DjangoProject.urls"

# Настройки шаблонов Django
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.debug',
            ],
        },
    },
]

# WSGI-приложение
WSGI_APPLICATION = "DjangoProject.wsgi.application"

# Настройки базы данных (SQLite по умолчанию, PostgreSQL через переменные окружения)
if config('USE_POSTGRESQL', default=False, cast=bool):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('POSTGRES_HOST', default='localhost'),
            'PORT': config('POSTGRES_PORT', default='5432'),
        }
    }
else:
    if amvera_var == '1':
        db_path = '/data/db.sqlite3'
    else:
        db_path = BASE_DIR / "db.sqlite3"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            # "NAME": BASE_DIR / "db.sqlite3",
            "NAME": db_path,
        }
    }

# Валидаторы паролей
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

# Конфигурация для логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': config('DJANGO_LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
    },
}

# Язык и часовой пояс проекта
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"

# Включение интернационализации и поддержки часовых зон
USE_I18N = True
USE_TZ = True

# Автоматическое поле первичного ключа по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройка Debug Toolbar
if DEBUG:
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    }

# Настройки для статических файлов
STATIC_URL = '/static/'  # URL для статических файлов
# STATICFILES_DIRS = [BASE_DIR / 'static', ]  # Директории со статическими файлами
STATIC_ROOT = BASE_DIR / 'static'  # Директория для сбора статических файлов

# Настройки для медиа-файлов
MEDIA_URL = '/media/'  # URL для медиа-файлов
MEDIA_ROOT = os.path.join(BASE_DIR, 'data/media')  # Директория для хранения медиа-файлов

# Настройки пользовательской модели пользователя
AUTH_USER_MODEL = 'users.CustomUser'

# ===== Настройки DRF =====
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# ===== Настройки документации API =====
SPECTACULAR_SETTINGS = {
    'TITLE': 'Authentication API',
    'DESCRIPTION': 'API для аутентификации пользователей',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/',
}

# ===== JWT Настройки =====
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# ===== CORS Настройки =====
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:8000,http://127.0.0.1:8000'
).split(',')

# ===== OAuth Настройки =====
OAUTH_PROVIDERS = {
    'vk': {
        'client_id': config('VK_OAUTH_CLIENT_ID', default=''),
        'client_secret': config('VK_OAUTH_CLIENT_SECRET', default=''),
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'token_url': 'https://oauth2.googleapis.com/token',
        'userinfo_url': 'https://www.googleapis.com/oauth2/v3/userinfo',
        'scopes': ['openid', 'email', 'profile'],
        'redirect_uri': config('VK_REDIRECT_URI', default='http://localhost:8000/oauth/google/callback/')
    },
    'yandex': {
        'client_id': config('YANDEX_OAUTH_CLIENT_ID', default=''),
        'client_secret': config('YANDEX_OAUTH_CLIENT_SECRET', default=''),
        'authorize_url': 'https://oauth.yandex.ru/authorize',
        'token_url': 'https://oauth.yandex.ru/token',
        'userinfo_url': 'https://login.yandex.ru/info',
        'scopes': ['login:email', 'login:info'],
        'redirect_uri': config('YANDEX_REDIRECT_URI', default='http://localhost/users/yandex_auth_callback')
    }
}

# URL для перенаправления после успешной OAuth-аутентификации
OAUTH_SUCCESS_REDIRECT_URL = config('OAUTH_SUCCESS_REDIRECT_URL', default='http://localhost:8000/login/success')
OAUTH_FAILURE_REDIRECT_URL = config('OAUTH_FAILURE_REDIRECT_URL', default='http://localhost:8000/login/error')

# ===== Настройки аутентификации =====
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',# Бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
    # 'authentication.oauth.backends.OAuthBackend',
]


# Настройки email
EMAIL_BACKEND = config('EMAIL_BACKEND')               # Используемый бекенд
EMAIL_HOST = config('EMAIL_HOST')                     # SMTP-сервер
EMAIL_PORT = config('EMAIL_PORT', cast=int)           # Порт для SMTP
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)    # Использование SSL
EMAIL_HOST_USER = config('EMAIL_HOST_USER')           # Логин SMTP
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')   # Пароль SMTP
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER                  # Email отправителя
SERVER_EMAIL = EMAIL_HOST_USER                        # Email для системных уведомлений
EMAIL_ADMIN = EMAIL_HOST_USER                         # Email администратора

# Настройки для представления аутентификации
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# LOGIN_URL = 'login'

# Настройки для сессий
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Использование базы данных для сессий
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Использует кэш для хранения сессий
# SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # Использует файлы для хранения сессий
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # Использует кэшированную базу данных для хранения сессий
SESSION_COOKIE_AGE = 1209600  # Время жизни сессии в секундах (2 недели)
SESSION_COOKIE_SECURE = False  # Установите True для HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'  # Настройка SameSite для сессионных cookie

# Внутренние IP-адреса для отладки
if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']
