from django.urls import path
from . import views
app_name = "chat_data"

urlpatterns = [
    path("", views.dashboard, name = "dashboard"),
    path("create_chat_room/", views.create_chat_room, name = "create_chat_room"),
    path("get_list_of_chat_rooms/", views.get_list_of_chat_rooms, 
         name = "get_list_of_chat_rooms"),
    path("<str:room_name>/", views.chat_room, name = "chat_room"),
    ]
