from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Deposite_Amount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)
    depo_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user} Deposites {self.amount}"
