from django.shortcuts import render
from .models import Movie,Crew
from rest_framework import viewsets
from .serializer import MovieSerializer,CrewSerializer
# Create your views here.


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CrewViewset(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer