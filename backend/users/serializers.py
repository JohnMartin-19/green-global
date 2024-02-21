from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "id",
        'name',
        "username",
        "email",
        "phone_number",
        "role",
        )
        model = CustomUser