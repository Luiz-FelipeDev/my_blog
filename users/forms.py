from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    ''' Realiza o Update das informações com relação a Class User'''
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    ''' Realiza o Update das informações com relação a Class Profile, nesse caso somente o campo de Image'''
    class Meta:
        model = Profile
        fields = ['image']
