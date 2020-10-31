from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=30)
    standard = models.IntegerField()
    rollNo = models.IntegerField()
    mobNo = models.CharField(max_length=10)