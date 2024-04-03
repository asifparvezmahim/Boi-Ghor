from django.contrib import admin
from django.urls import path, include
from account import views
from account.views import return_book


urlpatterns = [
    path("return_book/<int:id>", views.return_book, name="return_book"),
    path("confirm_borrow/<int:id>", views.confirm_purch, name="confirm_purch"),
]
