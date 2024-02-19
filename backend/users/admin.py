from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "is_staff",'role','name']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",'role','email','phone_number',)}),)
    
admin.site.register(CustomUser, CustomUserAdmin)    
