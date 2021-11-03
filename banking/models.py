from django.db import models
# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=15)
    balance = models.IntegerField()