import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "url_shortener_service.settings")

application = get_asgi_application()
