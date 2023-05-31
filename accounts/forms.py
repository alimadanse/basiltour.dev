from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CusomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', )پ
        fields = ('username' ,'phone_number', )
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = UserChangeForm.Meta.fields 
        