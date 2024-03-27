from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"<User : {self.user}> have a balance of <Amount: {self.balance} Taka>"
