from django.db import models
from users.models import CustomUser
from products.models import Product
# Create your models here.
class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField(default=0)
    time = models.TimeField(auto_now_add=True)