from .base import *

# Modo debug desactivado
DEBUG = False

# Hosts permitidos (reemplaza con tu dominio)
ALLOWED_HOSTS = ['tutienda.com', 'www.tutienda.com']

# Configuración de seguridad
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

