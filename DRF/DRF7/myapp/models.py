from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.CharField(max_length=10)