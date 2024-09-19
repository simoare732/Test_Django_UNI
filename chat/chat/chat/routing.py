from django.urls import path
from .consumers import WSConsumerChat


ws_urlpatterns = [
    path("ws/chatws/", WSConsumerChat.as_asgi()),
]