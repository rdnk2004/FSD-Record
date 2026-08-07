# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Flight, Booking

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'airline', 'origin', 'destination', 'departure_time', 'arrival_time', 'price', 'available_seats')
    search_fields = ('flight_number', 'airline', 'origin', 'destination')
    list_filter = ('airline', 'origin', 'destination')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'passenger_name', 'passenger_email', 'flight', 'seats_booked', 'booking_date', 'status')
    search_fields = ('passenger_name', 'passenger_email', 'flight__flight_number')
    list_filter = ('status', 'booking_date')
