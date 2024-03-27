from django import forms
from django.contrib.auth.models import User
from .models import Deposite_Amount


class DepoForm(forms.ModelForm):
    class Meta:
        model = Deposite_Amount
        fields = ["amount"]
