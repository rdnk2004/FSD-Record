# pyrefly: ignore [missing-import]
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.name)
