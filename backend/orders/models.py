from django.db import models
from users.models import CustomUser

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    product_id = models.ManyToManyField('products.Product', blank=True)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField(default=0)
    time = models.TimeField(auto_now_add=True)