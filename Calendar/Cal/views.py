from django.shortcuts import render
from .models import Event

def events(request):

    return render(request, 'events.html', {})

