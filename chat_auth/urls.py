from django.urls import path
from . import views
app_name = "chat_auth"
urlpatterns = [
    path("login_user/", views.login_user, name="login_user"),
    path("log_out/", views.log_out, name = "log_out"),
    path('register/', views.register, name='register'),
    path("change_password/", views.change_password, name = "change_password"),
    path("change_username/", views.change_username, name = "change_username"),
    path("change_email/", views.change_email, name = "change_email"),
    path("send_secret_key/", views.send_secret_key, name = "send_secret_key")
]