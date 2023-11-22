from .settings import *
import os

ALLOWED_HOSTS = ["*"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME", "whatsappPartnersDB"),
        'USER': os.getenv("DB_USER", "whatsappPartnersAdmin"),
        'PASSWORD': os.getenv("DB_PASSWORD", "aD5%w12Gx_&8"),
        'HOST': "postgres-partners",  # Use the service name from docker-compose.yml
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        'LOCATION': os.getenv("REDIS_HOST"),  # Use the REDIS_HOST environment variable
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_password")
