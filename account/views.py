from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from balance.models import Balance
from deposite.models import Deposite_Amount
from cart.models import Cart
from book.models import Book
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user.id
    balance = Balance.objects.get(user=request.user).balance
    user = request.user
    depo_history = Deposite_Amount.objects.filter(user=user)
    cart_show = Cart.objects.filter(user=user)
    return render(
        request,
        "profile.html",
        {"balance": balance, "depos": depo_history, "carts": cart_show},
    )


def register(request):
    if request.method == "POST":
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            # user_name = register_form.cleaned_data["username"]
            amnt = int(0)
            balance = Balance.objects.create(user=user, balance=amnt)
            balance.save()
            print("Username : ", user)
            return redirect("register")
    else:
        register_form = forms.RegistrationForm()
    return render(request, "register.html", {"form": register_form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                return redirect("homepage")

            else:
                return redirect("register")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("homepage")


@login_required
def make_bill(request, id):
    user_first_name = request.user.first_name
    user_last_name = request.user.last_name
    user_email = request.user.email
    book_name = Book.objects.get(id=id).title
    book_price = Book.objects.get(id=id).borrowing_price
    print(user_first_name, user_last_name, user_email, book_name, book_price)
    return render(
        request,
        "bill.html",
        {
            "uf_name": user_first_name,
            "ul_name": user_last_name,
            "uemail": user_email,
            "bname": book_name,
            "bprice": book_price,
            "bid": id,
        },
    )


@login_required
def confirm_purch(request, id):
    user = request.user
    if user.is_authenticated == False:
        return redirect("login")
    book_price = int(Book.objects.get(id=id).borrowing_price)
    user_balance = Balance.objects.get(user=user).balance
    if user_balance < book_price:
        messages.error(request, "Sorry You Do Not HAve Sufficient Balance")
    else:
        messages.success(
            request, "Congratulations !!! Successully Borrowing is Completed"
        )
        book = Book.objects.get(id=id)
        cart = Cart.objects.create(user=user, book=book)
        cart.save()
        new_balance = user_balance - book_price
        Balance.objects.filter(user=user).update(balance=new_balance)
    return redirect("profile")


@login_required
def return_book(request, id):
    user = request.user
    book_price = int(Cart.objects.get(id=id).book.borrowing_price)
    user_balance = Balance.objects.get(user=user).balance
    new_balance = user_balance + book_price
    Balance.objects.filter(user=user).update(balance=new_balance)
    Cart.objects.get(id=id).delete()
    messages.success(
        request,
        "Book Returned Successfully and The Book Borrowing Amount is Added to Your Account ",
    )
    return redirect("profile")


@login_required
def passChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.cleaned_data["user"])
            return redirect("prpfile")

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "infoChange.html", {"form": form})
