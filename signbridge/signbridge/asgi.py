import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

# Importación absoluta del consumer
from signbridge.communicator.consumers import SignBridgeConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signbridge.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/signbridge/", SignBridgeConsumer.as_asgi()),
    ]),
})