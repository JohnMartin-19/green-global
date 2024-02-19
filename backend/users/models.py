from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here

ROLE_CHOICES = (
    ('Buyer','Buyer'),
    ('Farmer','Farmer')
)
class User(AbstractUser):
    username = models.CharField(max_length=128,unique = True)
    email = models.EmailField(('email address'), unique=True)
    password = models.CharField(max_length=96,unique = True)
    phone = models.IntegerField(null = True)
    address = models.CharField(max_length=500,null = True)
    orders = models.CharField(max_length = 60)
    role = models.CharField(choices = ROLE_CHOICES,max_length = 10,default = '---')