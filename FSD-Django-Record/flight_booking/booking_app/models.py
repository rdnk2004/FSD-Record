# pyrefly: ignore [missing-import]
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20, unique=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.flight_number} ({self.source} -> {self.destination})"

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=20, unique=True)
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name} ({self.passport_number})"

class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='bookings')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        unique_together = ('passenger', 'flight')

    def __str__(self) -> str:
        return f"{self.passenger.name} - {self.flight.flight_number}"
