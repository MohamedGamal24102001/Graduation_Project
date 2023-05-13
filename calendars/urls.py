from django.urls import path
from .views import calendar , events

urlpatterns = [
    path('', calendar, name='calendar'),
    path('events/', events, name='events'),
]
