from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(
        max_length=200, required=True, widget=forms.PasswordInput)


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]
