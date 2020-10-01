from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PaymentDetails(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.IntegerField()
	currency = models.CharField(max_length = 50)
	receipt = models.CharField(max_length = 50)
	orderid = models.CharField(max_length = 100)
	status = models.CharField(max_length = 50)
