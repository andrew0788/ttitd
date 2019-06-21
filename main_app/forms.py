from django import forms
from django.forms import ModelForm
from django.contrib import auth

from .models import Profile, User, Trip_Report

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'profile_name',
            'location',
            'gender',
            'age',
            'weight',
            'bio',
            'social_link',
            'ghost_key'
        )

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip_Report
        fields = (
            'trip_name',
            'text_content',
            'date',
            'method',
            'other_drugs_taken',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Trip_Report
        fields = (
            'trip_name',
            'text_content',
            'date',
            'method',
            'other_drugs_taken',
            'effects'
        )

