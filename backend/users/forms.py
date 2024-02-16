from django.contrib.auth.forms import UserChangeForm,   UserCreationForm
from .models import Buyer,Farmer

class  BuyerSignUpForm(UserCreationForm):
    class Meta():
        model = Buyer
        fields = ['username', 'email','phone']
class BuyerUpdateForm(UserChangeForm):
    class Meta():
        model = Buyer
        fields = ['username', 'email','phone']
            
class FarmerSignupForm(UserCreationForm):
    class Meta():
        model = Farmer
        fields = ['username','email','phone','farm_name','location']
class FarmerUpdateForm(UserChangeForm):
    class Meta():
        model= Farmer
        fields = ['username','email','phone','farm_name','location']