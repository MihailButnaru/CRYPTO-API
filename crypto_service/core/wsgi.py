import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Base')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
