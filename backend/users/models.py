from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here

ROLE_CHOICES = (
    ('Buyer','Buyer'),
    ('Farmer','Farmer')
)
class CustomUser(AbstractUser):

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    name = models.CharField(null=True, blank=True, max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)
    

    def __str__(self):
        return self.name