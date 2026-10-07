from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)




class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
