from django.db import models

# Create your models here.
class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey('products.Product',on_delete = models.CASCADE)
    user = models.ForeignKey( 'users.CustomUser', on_delete=models.CASCADE, null=True) 
    review_message = models.CharField(max_length = 200)
    rating = models.PositiveIntegerField(null = True)
    review_date = models.DateTimeField(auto_now_add=True)