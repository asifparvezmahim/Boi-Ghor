from django.shortcuts import render
from book.views import Book


# Create your views here.
def home(request):
    top_books = Book.objects.all()[:3]
    print("Top Books: ", top_books)
    return render(request, "home.html", {"tops": top_books})
