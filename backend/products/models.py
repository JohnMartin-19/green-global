from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.IntegerField(primary_key=True,editable=False)
    product_name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    quantity = models.CharField(max_length=50)  # can be a number or text like "dozen"
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_out_of_stock = models.BooleanField(default=False)
   
    def __str__(self):
        return self.product_name + ' - KSH ' + str(self.price)
