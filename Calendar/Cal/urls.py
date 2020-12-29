from django.urls import path
from . import views

app_name = 'Cal'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    path('event/<int:pk>/remove', views.EventDelete.as_view(), name="rem_event"),
]