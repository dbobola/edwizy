from django.urls import re_path
from .consumers import StrategyConsumer

websocket_urlpatterns = [
    re_path(r'ws/strategies/$', StrategyConsumer.as_asgi()),
]
