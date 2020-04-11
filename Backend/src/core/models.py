# from django.db import models
from djongo import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class UserData(models.Model):
    name = models.CharField(verbose_name="name",max_length=100, default="NA")
    amount = models.FloatField(verbose_name="amount", default=0.0)
    cashflow = models.CharField(verbose_name="cashflow",max_length=2, default="NA") #I/E
    category = models.CharField(verbose_name="category",max_length=2, default="NA") #F/R/I
    interval = models.CharField(verbose_name="interval",max_length=2, default="N") #D/W/F/M/Q/H/Y/N
    description = models.TextField(verbose_name="description", default="NA")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name