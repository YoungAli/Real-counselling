from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label=("Enter a password"), strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password Confirmation"), strip=False, widget=forms.PasswordInput)

    class Meta:
        fields = ('matric_number', 'email', 'first_name', 'last_name')
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = ('first_name', 'last_name')
        model = CustomUser
