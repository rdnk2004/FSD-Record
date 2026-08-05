# pyrefly: ignore [missing-import]
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return str(self.name)

class Course(models.Model):
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    credits = models.IntegerField()

    def __str__(self) -> str:
        return str(self.name)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.student} - {self.course}"
