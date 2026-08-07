# pyrefly: ignore [missing-import]
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.flight_number} - {self.airline} ({self.origin} -> {self.destination})"

class Booking(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    passenger_phone = models.CharField(max_length=20)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    seats_booked = models.IntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Confirmed')
    objects = models.Manager()

    def __str__(self) -> str:
        return f"Booking #{self.id} - {self.passenger_name} ({self.flight.flight_number})"
