# coding: utf-8
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from calendar import HTMLCalendar
from datetime import datetime, date
from itertools import groupby
from django.utils.safestring import mark_safe

from .models import Event

class Calendar(HTMLCalendar):

    def __init__(self, workouts):
        super(Calendar, self).__init__()  # nie wiem o co chodzi z super
        self.workouts = self.group_by_day(workouts)

    def formatday(self, day, weekday):
        if day != 0:
            rok = date.today().year
            miesiac = date.today().month
            cssclass = self.cssclasses[weekday]
            if date.today() == date(rok, miesiac, day):  # dodanie klasy dla dnia dzisiejszego
                cssclass += ' dzis'
            if day in self.workouts:  # dodanie klasy dla dni kiedy byl dodany wpis
                cssclass += ' wpis'
                linkp = []  # lista w ktorej jest poczatek odnosnika
                linkk = []  # lista w  ktorej jest koniec odnosnika
                for workout in self.workouts[day]:  # dodanie adresu do dni kiedy byl wpis
                    linkp.append('<a href="%s">' % workout.get_absolute_url())
                    linkk.append('</a>')
                return self.day_cell(cssclass, '%s %s %s' % (
                ''.join(linkp), day, ''.join(linkk)))  # join podobnie jak w formacie miesiaca
            return self.day_cell(cssclass, day)
        else:
            return '<td class="noday">&nbsp;</td>'

    def day_cell(selfself, cssclass, body):  # funkcja dla dni zeby za kazdym razem nie pisac html
        return '<td class="%s">%s</td>' % (cssclass, body)

    def formatmonth(self, theyear, themonth, withyear=True):  # funkcja dla formatu miesiaca z templates.py
        v = []
        a = v.append
        a('<table class="table table-striped table-bordered">')  # tutaj zmiana na tabele bootstrapa
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
        a('</table>')
        return ''.join(v)

    def group_by_day(self, workouts):  # fukcja dla grupowania
        field = lambda workout: workout.data_pub.day  # pole z modelu gdzie jest data
        return dict(
            [(day, list(items)) for day, items in groupby(workouts, field)]
        )


def paginacja(strona, zmienna):  # paginacja
    paginator = Paginator(zmienna, 10)
    try:
        page_filter = paginator.page(strona)
    except PageNotAnInteger:
        page_filter = paginator.page(1)
    except EmptyPage:
        page_filter = paginator.page(paginator.num_pages)
    return page_filter


def events(request):

    page = request.GET.get('page')

    wszystkie = Event.objects.all().order_by('-data_pub')

    page_filter = paginacja(page, wszystkie)

    arg = {}  # potrzebne do wyszukiwania ajaxa
    arg.update(csrf(request))

    # nie przyszedl mi do glowy inny pomysl jak to napisac
    year = date.today().year
    month = date.today().month
    my_workouts = Event.objects.order_by('data_pub').filter(data_pub__year=year, data_pub__month=month)
    cal = Calendar(my_workouts).formatmonth(year, month)

    return render(request, 'events.html', {'page_filter': page_filter, 'arg': arg, 'cal': mark_safe(cal)})

