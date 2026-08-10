from django.shortcuts import render
from. models import Flight
# Create your views here.

def flight_list(request):
    flights = Flight.objects.all()
    return render (request, 'flights/flights.html', {'flights':flights})
    