from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializers import CountrySerializer
from .models import Country
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
# # Create your views here.


#------------------------------ModelViewset API-----------------
class CountryModelViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]


#----------------------------ResdOnly ModelViewset API-------------
class CountryReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
