# Cal/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime, date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta

import calendar
from .models import *
from .utils import Calendar
from .forms import EventForm, AddMember


@login_required(login_url='login')
def index(request):
    return HttpResponse('Kalendarz w Django')


def get_date(day):
    if day:
        year, month = (int(x) for x in day.split('-'))
        return date(year, month, day=1)

    return datetime.today()


def previous_month(day):
    first = day.replace(day=1)
    previous_month = first - timedelta(days=1)
    month = 'month=' + str(previous_month.year) + '-' + str(previous_month.month)

    return month


def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)

    return month


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    login_url = 'login'
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        day = get_date(self.request.GET.get('month', None))
        cal = Calendar(day.year, day.month)
        html_cal = cal.formatmonth(withyear=True)

        context['calendar'] = mark_safe(html_cal)
        context['previous_month'] = previous_month(day)
        context['next_month'] = next_month(day)

        return context


@login_required(login_url='login')
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        event_text = form.cleaned_data['event_text']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            event_text=event_text,
            start_time=start_time,
            end_time=end_time
        )
        return HttpResponseRedirect(reverse('Cal:calendar'))
    return render(request, 'event.html', {'form': form})


@login_required(login_url='login')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)


def add_eventmember(request, event_id):
    forms = AddMember()
    if request.method == 'POST':
        forms = AddMember(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data['user']
                #email = forms.cleaned_data['email']
                #action = forms.cleaned_data['action']
                EventMember.objects.create(
                    event=event,
                    user=user,
                    #email=email,
                    #action=action
                )
                return redirect('Cal:calendar')
            else:
                print('### Osiągnięto limit członków! ###')
    context = {
        'form': forms
    }
    return render(request, 'add-member.html', context)

class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'event_text', 'start_time', 'end_time']
    template_name = 'event.html'

class EventDelete(generic.DeleteView):
    model = EventMember
    template_name = 'event-delete.html'
    success_url = reverse_lazy('Cal:calendar')

