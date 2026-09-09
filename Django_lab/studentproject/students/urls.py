from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student/add/', views.student_create, name='student_create'),
]
