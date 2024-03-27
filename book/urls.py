from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("all_books/", views.all_books, name="all_books"),
    path("details/<int:id>", views.details.as_view(), name="details"),
    path("category/<slug:category_slug>/", views.all_books, name="cat_wise_post"),
]
