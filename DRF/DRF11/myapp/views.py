from django.shortcuts import render
from .models import Students
from .serializes import StudentSerializer
from rest_framework.generics import ListCreateAPIView
from .pagination import StudentPagination,StudentLimitffsetPagination
# from rest_framework.pagination import PageNumberPagination
# Create your views here.

class StudentsView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = StudentPagination
    pagination_class = StudentLimitffsetPagination
