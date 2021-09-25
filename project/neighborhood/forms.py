from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['Admin', 'pub_date', 'admin_profile']
        widgets = {
          'address': forms.Textarea(attrs={'rows':1, 'cols':10,}),
        }

