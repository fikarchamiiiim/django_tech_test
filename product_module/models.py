from django.db import models
from engine.models import Module

class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)