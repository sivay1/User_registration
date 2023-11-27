from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Userdata

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Userdata
        fields = ('username','email','password1','password2','first_name','last_name','profile_picture','address_line','city','state','pincode')
        



