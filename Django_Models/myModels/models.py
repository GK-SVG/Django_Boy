from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#_-----------Abstract Class(This class does not affects database)-----------------------
class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    class Meta:
        abstract = True

#----------------Inheriting Abstract Class--------
class Student(CommonInfo):
    cla = models.IntegerField()
    fee = models.IntegerField()


#---------------------Multiple Inheritance--------------------------
class ExamCenter(models.Model):
    code = models.CharField(max_length=6, unique=True)
    center = models.CharField(max_length=100)

class AdmitCard(ExamCenter,CommonInfo):
    cla = models.IntegerField()
    school = models.CharField(max_length=100)


#***************Model Realationship********************************
# ---------------One to One  Realationship-------------------------
class Post(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)




