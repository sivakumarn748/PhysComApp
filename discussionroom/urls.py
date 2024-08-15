from django.urls import path
from . import views

app_name = "dcsroom"

urlpatterns = [
    path('', view=views.home, name="home"),
    path('register-room/', view=views.Register_room.as_view(), name="register-room"),
    path('join-room/', view=views.Join_room.as_view(), name="join-room"),
    path('visit-room/<str:roomid>/', view=views.visit_room, name="visit-room")
]