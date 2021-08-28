import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from home.consumers import TestConsumer, NewConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChannelsCourse.settings')
application = get_asgi_application()

ws_patterns=[
    path('ws/testpath/', TestConsumer.as_asgi()),
    path('ws/newpath/', NewConsumer.as_asgi())

]
application=ProtocolTypeRouter({
    # "http": get_asgi_application(),
    'websocket':URLRouter(ws_patterns)
})