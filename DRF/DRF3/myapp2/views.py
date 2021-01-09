from django.shortcuts import render
from rest_framework.response import Response
from myapp.models import Product
from myapp.serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class ProductAPI(APIView):
    def get(self, request,id=None,format=None):
        if id is not None:
            prod = Product.objects.get(id=id)
            serializer = ProductSerializer(prod)
            return Response(serializer.data,status=status.HTTP_200_OK)
        prods = Product.objects.all()
        serializer = ProductSerializer(prods,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created successfully'},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    def put(self, request,id,format=None):
        prod = Product.objects.get(id=id)
        serializer = ProductSerializer(prod,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request,id,format=None):
        prod = Product.objects.get(id=id)
        serializer = ProductSerializer(prod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id,format=None):
        try:
            prod = Product.objects.get(id=id)
        except:
            return Response({'error':"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
        prod.delete()
        return Response({'msg':'data Deleted'})