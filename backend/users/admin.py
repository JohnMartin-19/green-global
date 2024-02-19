from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .forms import UserUpdateForm,UserCreateForm
from .models import User
# Register your models here.

class User_Admin(UserAdmin):
    add_form = UserCreateForm
    form = UserUpdateForm
    model = User
    list_display = ['username', 'email','phone','is_staff','role']

fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("username",)}),)
add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("username",'email','phone',"password","role")}),)
admin.site.register(User, User_Admin)
