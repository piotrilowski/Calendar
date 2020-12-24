from django.urls import path
from . import views

app_name = 'Cal'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
]