from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .forms import UserUpdateForm,UserCreateForm
from .models import User
# Register your models here.

class User_Admin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    model = User
    list_display = ['username', 'email','phone','is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
admin.site.register(User, User_Admin)
