"""
ASGI config for SolecitoCrochet project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from pathlib import Path

# Agregar la carpeta "apps" al PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent
os.sys.path.append(str(BASE_DIR / 'apps'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SolecitoCrochet.settings.base')  # Asegurarnos que apunte a SolecitoCrochet

application = get_asgi_application()
