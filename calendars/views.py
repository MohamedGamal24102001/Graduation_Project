from django.shortcuts import render
from .models import Event
from django.http import JsonResponse
from django.utils import timezone

def calendar(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'calendar.html', context)



def events(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    events = Event.objects.filter(start_time__range=(start_date, end_date))
    event_data = [{'title': event.title, 'start_date': event.start_time.date().isoformat()} for event in events]
    return JsonResponse(event_data, safe=False)
