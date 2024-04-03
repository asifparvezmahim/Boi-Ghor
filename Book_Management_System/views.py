from django.shortcuts import render
from book.views import Book
from cart.models import Cart


# Create your views here.
def home(request):
    top_books = Book.objects.all()[:3]
    return render(request, "home.html", {"tops": top_books})
