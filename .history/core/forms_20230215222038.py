from django import forms 
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserCreationForm
        fields = ['username', 'email', 'password1', 'password2']