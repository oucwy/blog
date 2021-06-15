"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

"""
	markwy
	2021.6.8
"""


import os

from django.core.wsgi import get_wsgi_application

# from . import appcfg

# markwy 21.6.12

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.develop')

application = get_wsgi_application()

