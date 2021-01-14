from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    Class = models.CharField(max_length=2)