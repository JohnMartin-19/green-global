from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
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
    password2 = models.CharField(max_length = 16,null = True)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)
    

    def __str__(self):
        return f"{self.name}"
    

def create_user(sender,instance,created, **kwargs):
    if created:
        CustomUser.objects.create(user = instance)
def save_user(sender, instance ,**kwargs):
    instance.save()

post_save.connect(create_user, sender=CustomUser)
post_save.connect(save_user, sender=CustomUser)