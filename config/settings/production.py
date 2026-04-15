from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-domain.com']  # Replace with your domain

# Production database
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'tryon_system',
    'USER': 'your_db_user',
    'PASSWORD': 'your_db_password',
    'HOST': 'localhost',
    'PORT': '3306',
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'