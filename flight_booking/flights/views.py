from django.shortcuts import render, redirect
from. models import Flight
# Create your views here.

def flight_list(request):
    flights = Flight.objects.all()
    return render (request, 'flights.html', {'flights':flights})

def update_flight(request, id):
    flight = Flight.objects.get(id=id)
    if request.method == 'POST':
        flight.name = request.POST['name']
        flight.destination = request.POST['destination']
        flight.departure_time = request.POST['departure_time']
        flight.save()
        return redirect('flight_list')
    return render(request, 'update_flight.html', {'flight': flight})