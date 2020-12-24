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