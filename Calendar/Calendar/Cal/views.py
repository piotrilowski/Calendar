from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Pierwszy widok w Django!")
