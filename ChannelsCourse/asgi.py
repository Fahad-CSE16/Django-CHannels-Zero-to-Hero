import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path,re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from home.consumers import TestConsumer, NewConsumer
from chatapp.consumers import ChatRoomConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChannelsCourse.settings')
application = get_asgi_application()

ws_patterns=[
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', chat_consumers.ChatConsumer.as_asgi()),
    path('ws/testpath/', TestConsumer.as_asgi()),
    re_path(r'ws/newpath/(?P<room_name>\w+)/$', NewConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatRoomConsumer.as_asgi())
    # path('ws/newpath/', NewConsumer.as_asgi())

]
#  For Local Server  use (For getting USER)
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                ws_patterns
            )
        ),
    ),
})

#  For WebsocketKing use
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": 
#         AuthMiddlewareStack(
#             URLRouter(
#                 ws_patterns
#             )
#         ),
    
# })