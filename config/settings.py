
from pathlib import Path
from datetime import timedelta
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

env.read_env(BASE_DIR / ".env")




# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

SECRET_KEY = env('SECRET_KEY',default='#$mysecretkey#$')

DEV = env.bool('DEV', default=True)

DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS',default=['localhost', '127.0.0.1'])

CORS_ALLOWED_ORIGINS = env.list(
    'CORS_ALLOWED_ORIGINS',
    default=[
        'http://localhost:3000',
        'http://127.0.0.1:3000',
    ]
)

CSRF_TRUSTED_ORIGINS = env.list(
    'CSRF_TRUSTED_ORIGINS',
    default=[
        'http://localhost:3000',
        'http://127.0.0.1:3000',
    ]
)




# SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)
# SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=False)
# CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=False)
# SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=0)



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders', # CORS
    # 'Authentication',
    'Authentication.apps.AuthenticationConfig',
    'drf_spectacular', #swagger
    'anymail', #email

    'cloudinary',
    'cloudinary_storage',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


DATABASES = {
    'default': env.db(
        'DATABASE_URL',
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'




# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = ''
# LOGIN_URL = '/login/'

AUTH_USER_MODEL = 'Authentication.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'Authentication.authentication.SessionJWTAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    'DEFAULT_THROTTLE_RATES': {
        'login': '10/hour',
        'verification': '10/hour',
        'register': '10/hour',
        'password-reset': '10/hour',
    },

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', # swagger


}

# swagger
SPECTACULAR_SETTINGS = {
    'TITLE': 'DRF Custom Auth API',
    'DESCRIPTION': 'Auto-generated API schema',
    'VERSION': '1.0.0',

    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATIONS': False,

    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'docExpansion': 'none',
        'defaultModelsExpandDepth': -1,
    },

    'SECURITY_SCHEMES': {
        'BearerAuth': {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
        }
    },
}


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1500),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'BLACKLIST_AFTER_ROTATION': True,
    'ROTATE_REFRESH_TOKENS': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
}




if DEV:
    EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
    EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
    EMAIL_PORT = env.int('EMAIL_PORT', default=587)
    EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
    EMAIL_TIMEOUT = env.int('EMAIL_TIMEOUT', default=60)
    EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='test@gmail.com')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='xxx-xxx-xxx')
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='test@gmail.com')

else:
    EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='test@gmail.com')
    ANYMAIL = {
        "BREVO_API_KEY": env('EMAIL_HOST_PASSWORD', default='xxx-xxx-xxx'),
    }

print(f'Email Backend: {EMAIL_BACKEND}')
print(f'DB: {DATABASES}')
print(f'allowed hosts: {ALLOWED_HOSTS}')
print(f'cookie domain: {CSRF_TRUSTED_ORIGINS}')




# Frontend URL for email sending verifications links
FRONTEND_URL = env('FRONTEND_URL', default='http://localhost:3000')


PASSWORD_RESET_TIMEOUT = env.int('PASSWORD_RESET_TIMEOUT', default=600)
OTP_EXPIRE_TIMEOUT = env.int('OTP_EXPIRE_TIMEOUT', default=600)
MAX_WRONG_OTP_ATTEMPTS = env.int('MAX_WRONG_OTP_ATTEMPTS', default=5)
OTP_LOCKED_UNTIL = env.int('OTP_LOCKED_UNTIL', default=600)
MAX_LOGIN_ATTEMPTS = env.int('MAX_LOGIN_ATTEMPTS', default=5)
ACCOUNT_LOCKOUT_DURATION = env.int('ACCOUNT_LOCKOUT_DURATION', default=600)

GEOLOCATION_ENABLED = env.bool('GEOLOCATION_ENABLED', default=True)
GEOLOCATION_TIMEOUT = env.int('GEOLOCATION_TIMEOUT', default=5)

LOGIN_HISTORY_RETENTION_DAYS = env.int('LOGIN_HISTORY_RETENTION_DAYS', default=90)
INACTIVE_SESSION_RETENTION_DAYS = env.int('INACTIVE_SESSION_RETENTION_DAYS', default=30)
TWO_FA_LOG_RETENTION_DAYS = env.int('TWO_FA_LOG_RETENTION_DAYS', default=30)



# ============================ Deployment ===========================

import cloudinary
import cloudinary.uploader
import cloudinary.api



if DEV:
    STORAGES = {
        'default': {
            'BACKEND': 'django.core.files.storage.FileSystemStorage',
        },
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
        },
    }
else:
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': env('CLOUDINARY_API_KEY'),
        'API_SECRET': env('CLOUDINARY_API_SECRET'),
    }

    STORAGES = {
        'default': {
            'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage',
        },
        'staticfiles': {
            'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
        },
    }