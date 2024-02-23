from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id', 
            'user', 
            'product_id',
            'quantity',
            'total_price',
            'time'
            )