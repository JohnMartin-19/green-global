from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .forms import BuyerSignUpForm,BuyerUpdateForm,FarmerSignupForm,FarmerUpdateForm
from .models import Buyer,Farmer
# Register your models here.

class BuyerAdmin(admin.ModelAdmin):
    add_form = BuyerSignUpForm
    form = BuyerUpdateForm
    model = Buyer
    list_display = ['username', 'email','phone']
     

class FarmerAdmin(admin.ModelAdmin):
    add_form = FarmerSignupForm
    form = FarmerUpdateForm
    model = Farmer
    list_display = ['username','email','phone','farm_name','location']
    
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Farmer, FarmerAdmin)