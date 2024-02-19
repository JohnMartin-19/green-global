from django.contrib.auth.forms import UserChangeForm,   UserCreationForm
from .models import User

class  UserCreateForm(UserCreationForm):
    class Meta():
        model =User
        fields = UserCreationForm.Meta.fields + ('username',)
class UserUpdateForm(UserChangeForm):
    class Meta():
        model = User
        fields = UserChangeForm.Meta.fields
            
