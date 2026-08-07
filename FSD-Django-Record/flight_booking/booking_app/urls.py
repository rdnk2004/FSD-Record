from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('manage/', views.manage_flights, name='manage_flights'),
    path('manage/edit/<int:flight_id>/', views.edit_flight, name='edit_flight'),
    path('manage/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
]
