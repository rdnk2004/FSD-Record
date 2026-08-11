from django.urls import path
from . import views
urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('update/<int:id>/', views.update_flight, name='update_flight'),
]