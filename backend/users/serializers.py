from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.password_validation import validate_password
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

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        token['email'] = user.email
        return token
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,required = True, validators = [validate_password])
    password2 = serializers.CharField(write_only = True, required=True)

    class Meta:
        model = CustomUser
        fields = ['email','username','password','password2']

        #check password match for validation

        def validate_pass(self,attrs):
            if attrs ['password'] != ['password2']:
                raise serializers.ValidationError({
                    'Password':'Passwords do not match'})
            return attrs
        #create user, after checking passwords
        def create(self, validate_data):
            user = CustomUser.objects.create(
                username = validate_data["username"],
                email = validate_data["email"],
                )
            user.set_password(validate_data['password'])
            user.save()
            return user