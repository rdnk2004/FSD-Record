# pyrefly: ignore [missing-import]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
    path('courses/', views.courses, name='courses'),
    path('edit-course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:id>/', views.delete_course, name='delete_course'),
    path('enrollment/', views.enrollment, name='enrollment'),
    path('edit-enrollment/<int:id>/', views.edit_enrollment, name='edit_enrollment'),
    path('delete-enrollment/<int:id>/', views.delete_enrollment, name='delete_enrollment'),
]
