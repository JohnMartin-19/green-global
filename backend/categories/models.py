from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length = 30)
