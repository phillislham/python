s("wsgi.py")
"""
WSGI config for learnlang project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# sirve archivos estaticos

# si activo esto en local se fastidia, me da un error de version
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnlang.settings')
application = get_wsgi_application()

# bug(application,"wsgi.py.application")
# application = DjangoWhiteNoise(application)