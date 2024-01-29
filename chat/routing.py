from django.urls import path
from .consumers import ChatConsumers

websocket_urlpatterns = [
    path('ws/<slug:room_name>/', ChatConsumers.as_asgi()),
]