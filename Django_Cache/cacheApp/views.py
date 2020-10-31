from django.shortcuts import render
from .models import StudentData
# Create your views here.
def mycache(request):
    students = StudentData.objects.all()
    return render(request,'cache.html',{'students':students})