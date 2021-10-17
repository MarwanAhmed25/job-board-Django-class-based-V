from django.forms import ModelForm
from django.core.exceptions import ValidationError
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
    class Meta:
        model = Profile
        fields = [
            'image',
            'code',
            'phone',
            'birthdate',
            'description'
        ]
    
    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        if birthdate is not None:
            today = date.today().year
            age = today - birthdate.year
            print(age, '....')
            if age < 20:
               raise ValidationError("age must be greater than 19!!")

            return birthdate

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone is not None:
           
            if len(phone) != 11:
               raise ValidationError("phone must be correct!!")

            return phone
