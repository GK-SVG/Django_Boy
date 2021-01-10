from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializers import CountrySerializer
from .models import Country
# Create your views here.


class CountryViewset(viewsets.ViewSet):
    def get(self,request):
        country = Country.objects.all()
        serializer = CountrySerializer(country,many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        country = Country.objects.get(id=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created','data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_NOT_FOUND)
    def put(self, request,pk):
        country = Country.objects.get(id=pk)
        serializer = CountrySerializer(country,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated','data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_NOT_FOUND)
    def destroy(self, request, pk):
        country = Country.objects.get(id=pk)
        country.delete()
        return Response({'msg':'Data Deleted Successfully'})


class CountryModelViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer