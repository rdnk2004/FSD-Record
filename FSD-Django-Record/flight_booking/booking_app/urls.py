from django.urls import path
from . import views

urlpatterns = [
    # User Authentication
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    # Dashboard & Search
    path('', views.dashboard, name='dashboard'),

    # Flight Management (CRUD)
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/add/', views.add_flight, name='add_flight'),
    path('flights/edit/<int:pk>/', views.edit_flight, name='edit_flight'),
    path('flights/delete/<int:pk>/', views.delete_flight, name='delete_flight'),

    # Passenger Management (CRUD)
    path('passengers/', views.passenger_list, name='passenger_list'),
    path('passengers/add/', views.add_passenger, name='add_passenger'),
    path('passengers/edit/<int:pk>/', views.edit_passenger, name='edit_passenger'),
    path('passengers/delete/<int:pk>/', views.delete_passenger, name='delete_passenger'),

    # Flight Booking Module
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/book/', views.book_flight, name='book_flight'),
    path('bookings/cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]
