from django.db import models
from django.conf import settings
from products.models import Products
# Create your models here
class Buyer(models.Model):
    buyer_id = models.IntegerField(primary_key=True,unique=True)
    username = models.CharField(max_length=128)
    email = models.EmailField(('email address'), unique=True)
    phone = models.IntegerField(unique=True)
    address = models.CharField(max_length=500,null = True)
    orders = models.CharField(max_length = 60)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class Farmer(models.Model):
    farmer_id =models.IntegerField(primary_key=True, editable=False)
    username = models.CharField(max_length=128)
    email = models.EmailField(('email address'), unique=True)
    phone = models.IntegerField(unique=True)
    address = models.CharField(max_length=500,null = True)
    farm_name = models.CharField(max_length=64)
    location = models.CharField(max_length=128) 
    