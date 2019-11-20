# users/forms.py
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Address
from django.forms.widgets import FileInput

class CustomUserCreationForm(UserCreationForm):
     class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
        labels = {
            'first_name': ('First Name:'),
            'last_name': ('Last Name:'),
        }

class CustomUserChangeForm(UserChangeForm):
    image = forms.ImageField(label=('Image'),required=False,
                                    error_messages ={'invalid':("Image files only")},
                                    widget= FileInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'image',)
        labels = {
            'first_name': ('First Name:'),
            'last_name': ('Last Name:'),
        }



class AddAdressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('addressLine1', 'addressLine2', 'suburbCity', 'country', 'stateProvince', 'zipCode', 'latitude', 'longitude')
