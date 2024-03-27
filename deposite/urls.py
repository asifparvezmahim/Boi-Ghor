from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("depo_money/", views.depo_money, name="depo_money"),
]
