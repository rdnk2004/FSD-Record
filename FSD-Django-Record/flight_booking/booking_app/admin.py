# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Flight, Passenger, Booking

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'source', 'destination', 'departure_date', 'price', 'available_seats')
    search_fields = ('flight_number', 'source', 'destination')
    list_filter = ('source', 'destination', 'departure_date')

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'passport_number')
    search_fields = ('name', 'email', 'passport_number')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'passenger', 'flight', 'booking_date')
    search_fields = ('passenger__name', 'flight__flight_number')
    list_filter = ('booking_date',)
