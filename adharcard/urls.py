from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.welcome, name="welcome"),
    path("signup", views.signup, name="signup"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("index/", views.index, name="index"),
    path("img_handle", views.img_handle, name="img_handle"),
]
