from django import forms
from django.contrib.auth.models import User
from map.models import shape_data
from django.contrib.auth.forms import UserCreationForm

class MapForm(forms.ModelForm):
    class Meta:
        model = shape_data
        fields = ["north","south","east","west"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
