from django.urls import path,re_path
from diet_app.views import join_room
urlpatterns = [

path("join_room/<int:id>", join_room, name="Join_room"),
]