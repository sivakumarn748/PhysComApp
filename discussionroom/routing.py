from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/dcsroom/<roomid>', consumers.ChatConsumer.as_asgi())
]