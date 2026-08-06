# pyrefly: ignore [missing-import]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('employees/', views.employees, name='employees'),
    path('edit-employee/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:id>/', views.delete_employee, name='delete_employee'),
]
