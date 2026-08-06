# pyrefly: ignore [missing-import]
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.name)
