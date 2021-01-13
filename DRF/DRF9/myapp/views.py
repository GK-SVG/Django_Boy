from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializers import CountrySerializer
from .models import Country
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle
from myapp.throtteling import MyRateThrotteler
# # Create your views here.


#------------------------------ModelViewset API-----------------
class CountryModelViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,MyRateThrotteler]
    
    
#----------------------------ResdOnly ModelViewset API-------------
class CountryReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
