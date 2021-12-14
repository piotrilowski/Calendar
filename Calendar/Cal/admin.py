from django.contrib import admin
from .models import Event, EventMember

# Register your models here.
# PL - Zarejestruj swoj model w tym miejscu

admin.site.register(Event)
admin.site.register(EventMember)
