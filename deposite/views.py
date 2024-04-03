from django.shortcuts import render, redirect
from . import forms
from .models import Deposite_Amount
from balance.models import Balance
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def depo_money(request):
    if request.method == "POST":
        depo_form = forms.DepoForm(request.POST)
        if depo_form.is_valid():
            str_amnt = depo_form.cleaned_data["amount"]
            amnt = int(str_amnt)
            user = request.user
            Deposite_Amount.objects.create(user=user, amount=amnt)
            user_balance = Balance.objects.get(user=user).balance
            new_balance = amnt + user_balance
            Balance.objects.filter(user=user).update(balance=new_balance)
            messages.success(request, f"{amnt} Taka is Deposited to Your Account")
            mail_subject = "Deposite Message"
            message = render_to_string(
                "depo_email.html",
                {
                    "user": request.user,
                    "depo_balance": amnt,
                    "new_balance": new_balance,
                },
            )
            to_email = request.user.email
            send_email = EmailMultiAlternatives(mail_subject, "", to=[to_email])
            send_email.attach_alternative(message, "text/html")
            send_email.send()
            return redirect("depo_money")
    else:
        depo_form = forms.DepoForm()
    return render(request, "depo.html", {"form": depo_form})
