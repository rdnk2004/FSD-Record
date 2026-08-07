# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Flight, Booking

def index(request):
    flights = Flight.objects.all()
    bookings = Booking.objects.all().order_by('-booking_date')

    search_query = request.GET.get('query', '').strip()
    origin_filter = request.GET.get('origin', '').strip()
    destination_filter = request.GET.get('destination', '').strip()

    if search_query:
        flights = flights.filter(
            flight_number__icontains=search_query
        ) | flights.filter(
            airline__icontains=search_query
        )

    if origin_filter:
        flights = flights.filter(origin__icontains=origin_filter)

    if destination_filter:
        flights = flights.filter(destination__icontains=destination_filter)

    origins = Flight.objects.values_list('origin', flat=True).distinct()
    destinations = Flight.objects.values_list('destination', flat=True).distinct()

    return render(request, 'index.html', {
        'flights': flights,
        'bookings': bookings,
        'origins': origins,
        'destinations': destinations,
        'search_query': search_query,
        'origin_filter': origin_filter,
        'destination_filter': destination_filter,
    })

def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        name = request.POST.get('passenger_name')
        email = request.POST.get('passenger_email')
        phone = request.POST.get('passenger_phone')
        seats = int(request.POST.get('seats_booked', 1))

        if flight.available_seats >= seats and seats > 0:
            Booking.objects.create(
                passenger_name=name,
                passenger_email=email,
                passenger_phone=phone,
                flight=flight,
                seats_booked=seats
            )
            flight.available_seats -= seats
            flight.save()
            messages.success(request, f"Flight {flight.flight_number} booked successfully for {name}!")
        else:
            messages.error(request, "Not enough available seats!")

    return redirect('index')

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    flight = booking.flight
    flight.available_seats += booking.seats_booked
    flight.save()
    booking.delete()
    messages.info(request, "Booking cancelled successfully.")
    return redirect('index')

def manage_flights(request):
    if request.method == 'POST':
        flight_number = request.POST.get('flight_number')
        airline = request.POST.get('airline')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        departure_time = request.POST.get('departure_time')
        arrival_time = request.POST.get('arrival_time')
        price = request.POST.get('price')
        available_seats = request.POST.get('available_seats')

        Flight.objects.create(
            flight_number=flight_number,
            airline=airline,
            origin=origin,
            destination=destination,
            departure_time=departure_time,
            arrival_time=arrival_time,
            price=price,
            available_seats=available_seats
        )
        messages.success(request, "New flight added successfully!")
        return redirect('manage_flights')

    flights = Flight.objects.all().order_by('departure_time')
    return render(request, 'manage_flights.html', {
        'flights': flights
    })

def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        flight.flight_number = request.POST.get('flight_number')
        flight.airline = request.POST.get('airline')
        flight.origin = request.POST.get('origin')
        flight.destination = request.POST.get('destination')
        flight.departure_time = request.POST.get('departure_time')
        flight.arrival_time = request.POST.get('arrival_time')
        flight.price = request.POST.get('price')
        flight.available_seats = request.POST.get('available_seats')
        flight.save()
        messages.success(request, f"Flight {flight.flight_number} updated successfully!")
        return redirect('manage_flights')

    flights = Flight.objects.all().order_by('departure_time')
    return render(request, 'manage_flights.html', {
        'flight': flight,
        'flights': flights,
        'edit_mode': True
    })

def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    flight_no = flight.flight_number
    flight.delete()
    messages.success(request, f"Flight {flight_no} deleted successfully!")
    return redirect('manage_flights')
