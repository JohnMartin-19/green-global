from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_name',
            'price',
            'is_out_of_stock',
            'description',
            'image',
            'order_id',
            'user',
            'category_id',
        )
        model = Product