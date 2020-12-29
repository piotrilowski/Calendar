from django.forms import ModelForm, DateInput
from django import forms
from Cal.models import Event, EventMember


class LogIn(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label='Hasło',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Hasło'}))

class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class AddMember(forms.ModelForm):
  class Meta:
    model = EventMember
    fields = ['user']