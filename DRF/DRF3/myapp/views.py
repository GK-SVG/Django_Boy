from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
# Create your views here.


@api_view()
def test_api(request):
    return Response({'msg':'this is test api'})


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def products_api(request,id=None):
    if request.method=='GET':
        if id is not None:
            prod = Product.objects.get(id=id)
            serializer = ProductSerializer(prod)
            return Response(serializer.data,status=status.HTTP_200_OK)
        prods = Product.objects.all()
        serializer = ProductSerializer(prods,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created successfully'},status=status.HTTP_201_CREATED)
        return Response({'msg':'Error'},status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PUT":
        prod = Product.objects.get(id=id)
        serializer = ProductSerializer(prod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        prod = Product.objects.get(id=id)
        serializer = ProductSerializer(prod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        prod = Product.objects.get(id=id)
        prod.delete()
        return Response({'msg':'data Deleted'})