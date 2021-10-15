from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from datetime import date

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]


class ProfileForm(ModelForm):
    def clean_birthday(self):
        if self.birthday is not None:
            today = date.today().year
            age = today - self.birthday.year
            print(age,'....')
            if age >= 20:
                self.age = age
                return self.age
        
    class Meta:
        model = Profile
        fields = [
            'image',
            'code',
            'phone',
            'birthdate',
            'description'
        ]
