from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.urls import reverse
from Cal.forms import LogIn, EventForm
from Cal.models import Event


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


def addevent(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        return HttpResponseRedirect(reverse('Cal:calendar'))
    return render(request, 'event.html', {'form': form})
