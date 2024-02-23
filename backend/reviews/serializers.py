from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_id',
            'user',
            'review_message',
            'rating',
            'review_date',
        )
        model = Review