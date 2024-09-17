from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.index, name="index"),
    path("FriXbyTes", views.welcome, name="welcome"),
    path("signup", views.signup, name="signup"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("img_handle", views.img_handle, name="img_handle"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("profile/", views.profile, name="profile"),
    path("userpf/", views.userpf, name="userpf"),
    path("testing/", views.testing, name="testing"),
]
