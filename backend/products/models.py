from django.db import models
from users.models import CustomUser
from orders.models import Order
from categories.models import  Category
# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=256)
    price = models.IntegerField(default = 0)
    is_out_of_stock = models.BooleanField(default =False)
    description = models.CharField(max_length = 200)
    image = models.ImageField(null = True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    order_id = models.ManyToManyField(Order)
    category_id = models.ForeignKey(Category,on_delete = models.CASCADE,null = True)