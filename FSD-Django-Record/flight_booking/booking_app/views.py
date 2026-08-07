# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flight, Passenger, Booking

# User Registration & Login Module
def register_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, f"Registration successful. Welcome, {username}!")
            return redirect('dashboard')

    return render(request, 'register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login_user')

# Search & Dashboard Module
@login_required
def dashboard(request):
    total_flights = Flight.objects.count()
    total_passengers = Passenger.objects.count()
    total_bookings = Booking.objects.count()

    source_query = request.GET.get('source', '').strip()
    dest_query = request.GET.get('destination', '').strip()
    date_query = request.GET.get('departure_date', '').strip()

    flights = Flight.objects.all()

    if source_query:
        flights = flights.filter(source__icontains=source_query)
    if dest_query:
        flights = flights.filter(destination__icontains=dest_query)
    if date_query:
        flights = flights.filter(departure_date=date_query)

    recent_bookings = Booking.objects.all().order_by('-booking_date')[:5]

    return render(request, 'dashboard.html', {
        'total_flights': total_flights,
        'total_passengers': total_passengers,
        'total_bookings': total_bookings,
        'flights': flights,
        'recent_bookings': recent_bookings,
        'source_query': source_query,
        'dest_query': dest_query,
        'date_query': date_query,
    })

# Flight Management (CRUD)
@login_required
def flight_list(request):
    flights = Flight.objects.all().order_by('departure_date')
    return render(request, 'flights.html', {'flights': flights})

@login_required
def add_flight(request):
    if request.method == 'POST':
        flight_number = request.POST.get('flight_number')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        departure_date = request.POST.get('departure_date')
        price = request.POST.get('price')
        available_seats = request.POST.get('available_seats')

        Flight.objects.create(
            flight_number=flight_number,
            source=source,
            destination=destination,
            departure_date=departure_date,
            price=price,
            available_seats=available_seats
        )
        messages.success(request, f"Flight {flight_number} added successfully!")
        return redirect('flight_list')
    return redirect('flight_list')

@login_required
def edit_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.flight_number = request.POST.get('flight_number')
        flight.source = request.POST.get('source')
        flight.destination = request.POST.get('destination')
        flight.departure_date = request.POST.get('departure_date')
        flight.price = request.POST.get('price')
        flight.available_seats = request.POST.get('available_seats')
        flight.save()
        messages.success(request, f"Flight {flight.flight_number} updated successfully!")
        return redirect('flight_list')

    flights = Flight.objects.all().order_by('departure_date')
    return render(request, 'flights.html', {
        'flight': flight,
        'flights': flights,
        'edit_mode': True
    })

@login_required
def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    flight_no = flight.flight_number
    flight.delete()
    messages.success(request, f"Flight {flight_no} deleted successfully!")
    return redirect('flight_list')

# Passenger Management (CRUD)
@login_required
def passenger_list(request):
    passengers = Passenger.objects.all().order_by('name')
    return render(request, 'passengers.html', {'passengers': passengers})

@login_required
def add_passenger(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        passport_number = request.POST.get('passport_number')

        Passenger.objects.create(
            name=name,
            email=email,
            phone=phone,
            passport_number=passport_number
        )
        messages.success(request, f"Passenger {name} added successfully!")
        return redirect('passenger_list')
    return redirect('passenger_list')

@login_required
def edit_passenger(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        passenger.name = request.POST.get('name')
        passenger.email = request.POST.get('email')
        passenger.phone = request.POST.get('phone')
        passenger.passport_number = request.POST.get('passport_number')
        passenger.save()
        messages.success(request, f"Passenger {passenger.name} updated successfully!")
        return redirect('passenger_list')

    passengers = Passenger.objects.all().order_by('name')
    return render(request, 'passengers.html', {
        'passenger': passenger,
        'passengers': passengers,
        'edit_mode': True
    })

@login_required
def delete_passenger(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    p_name = passenger.name
    passenger.delete()
    messages.success(request, f"Passenger {p_name} deleted successfully!")
    return redirect('passenger_list')

# Flight Booking Module
@login_required
def booking_list(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    passengers = Passenger.objects.all().order_by('name')
    flights = Flight.objects.filter(available_seats__gt=0).order_by('departure_date')
    return render(request, 'bookings.html', {
        'bookings': bookings,
        'passengers': passengers,
        'flights': flights,
    })

@login_required
def book_flight(request):
    if request.method == 'POST':
        passenger_id = request.POST.get('passenger')
        flight_id = request.POST.get('flight')

        passenger = get_object_or_404(Passenger, id=passenger_id)
        flight = get_object_or_404(Flight, id=flight_id)

        # Check for Duplicate Booking
        if Booking.objects.filter(passenger=passenger, flight=flight).exists():
            messages.error(request, f"Duplicate Booking Error: Passenger '{passenger.name}' is already booked on Flight {flight.flight_number}!")
            return redirect('booking_list')

        # Check Available Seats
        if flight.available_seats <= 0:
            messages.error(request, f"Flight {flight.flight_number} has no available seats left!")
            return redirect('booking_list')

        # Create Booking & Decrement Seat Count
        Booking.objects.create(passenger=passenger, flight=flight)
        flight.available_seats -= 1
        flight.save()

        messages.success(request, f"Successfully booked Flight {flight.flight_number} for Passenger '{passenger.name}'!")
        return redirect('booking_list')

    return redirect('booking_list')

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    flight = booking.flight
    flight.available_seats += 1
    flight.save()
    booking.delete()
    messages.info(request, "Booking cancelled successfully.")
    return redirect('booking_list')
