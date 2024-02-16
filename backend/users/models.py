from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class  CustomUser(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField(('email address'), unique=True)
    phone = models.IntegerField(unique=True,max_length=13)
    address = models.CharField(max_length=500)

class Buyer(CustomUser):
    orders = models.ForeignKey('Order', on_delete=models.CASCADE)
    def __str__(self):
        return self.username
class Farmer(CustomUser):
    farm_name = models.CharField(max_length=64)
    products = models.ForeignKey("Product",on_delete=models.CASCADE)
    location = models.CharField(max_length=128) 

    def __str__(self):
        return self.farm_name + " - " + self.location
    