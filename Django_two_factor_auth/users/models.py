from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustumUser(AbstractUser):
    phone = models.CharField(max_length=13)
    
