from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register-user/', view=views.Register.as_view(), name="register-user"),
    path('login-user/', view=views.Login.as_view(), name="login-user"),
]
