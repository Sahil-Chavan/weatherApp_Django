from django import forms
from django.forms import ModelForm
from .models import *

class AuthForm(forms.ModelForm):
    
    class Meta:
        model = Credentials
        fields = '__all__'
