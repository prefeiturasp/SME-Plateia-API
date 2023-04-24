from .base import *
from .base import env

# https://docs.djangoproject.com/en/dev/ref/settings/#debug

DEBUG = env('DJANGO_DEBUG', default=True)

# https://pypi.org/project/django-cors-headers/

CORS_ORIGIN_ALLOW_ALL = True
