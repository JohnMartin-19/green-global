from django.db import models
import uuid
# Create your models here
class Buyer(models.Model):
    buyer_id = models.UUIDField(primary_key=True,default = uuid.uuid4,editable = False)
    username = models.CharField(max_length=128)
    email = models.EmailField(('email address'), unique=True)
    phone = models.IntegerField(unique=True)
    address = models.CharField(max_length=500)
    orders = models.CharField(max_length = 60)
    def __str__(self):
        return self.username
class Farmer(models.Model):
    farmer_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=128)
    email = models.EmailField(('email address'), unique=True)
    phone = models.IntegerField(unique=True)
    address = models.CharField(max_length=500)
    farm_name = models.CharField(max_length=64)
    location = models.CharField(max_length=128) 

    def __str__(self):
        return self.farm_name + " - " + self.location
    