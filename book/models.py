from django.db import models
from category.models import Category
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to="book/cover_image/")
    borrowing_price = models.CharField(max_length=10)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments", blank=True, null=True
    )
    Comment_Box = models.TextField(max_length=25)
    time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"Comment From : {self.request.user.first_name} {self.request.user.last_name}"
