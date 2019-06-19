from django import forms
from django.forms import ModelForm
from django.contrib import auth
from .models import Profile, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_name',
            'location',
            'gender',
            'age',
            'weight',
            'bio',
            'social_link',
            'ghost_key'
        ]
