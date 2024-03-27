from django.contrib import admin
from django.urls import path, include
from account import views
from account.views import return_book

urlpatterns = [
    path("add_to_cart/<int:id>", views.add_to_cart, name="add_to_cart"),
    path("return_book/<int:id>", views.return_book, name="return_book"),
]
