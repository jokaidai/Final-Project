from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

class CustomUserCreationForm(UserCreationForm):    
    class Meta: 
        model = User
        fields = ("username", "password1", "password2", "email", )