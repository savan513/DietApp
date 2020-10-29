from django.conf.urls import url
from django.urls import re_path

from . import consumer


websocket_urlpatterns = [

    url(r'ws/diet_chat/(?P<room_name>\w+)/$', consumer.ChatConsumer),

]