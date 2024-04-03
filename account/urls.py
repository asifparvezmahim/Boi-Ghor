from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("info_change", views.passChange, name="info_change"),
    path("bill/<int:id>", views.make_bill, name="make_a_bill"),
]
