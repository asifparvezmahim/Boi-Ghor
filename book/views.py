from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from . import forms
from category.models import Category


# Create your views here.
def all_books(request, category_slug=None):
    all_books = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        all_books = Book.objects.filter(category=category)
        print("Category: ", category)
        print("Filtered: ", all_books)
    categories = Category.objects.all()
    return render(request, "show_book.html", {"books": all_books, "cats": categories})


class details(DetailView):
    model = Book
    pk_url_kwarg = "id"
    template_name = "details.html"

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        book = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        comments = book.comments.all()
        comment_form = forms.CommentForm()
        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
