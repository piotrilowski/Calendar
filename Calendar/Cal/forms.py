from django.forms import ModelForm, DateInput
from Cal.models import Event, EventMember
from django import forms

class LogIn(forms.Form):
  username = forms.CharField(label = 'Nazwa użytkownika', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa użytkownika'}))
  password = forms.CharField(label = 'Hasło', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}))



