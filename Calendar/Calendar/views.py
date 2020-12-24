from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Cal.forms import LogIn

def user_login(request):

    forms = LogIn()

    if request.method == 'POST':
        forms = LogIn(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                return redirect('Cal:calendar')
    context = {'form': forms}

    return render(request, 'login.html', context)

def user_logout(request):

    logout(request)
    return redirect('login')