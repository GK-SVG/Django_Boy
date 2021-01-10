"""DRF3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import products_api
from myapp2.views import (ProductAPI,DeleteProductAPI,
                         RetrieveProductAPI,ListProductAPI,
                         CreateProductAPI,UpdateProductAPI,
                         GetPostProductAPI,RetrievePutDeleteProductAPI,ProductListCreate,
                         ProductRetrieveUpdateDestroy)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('testapi/',views.test_api),
    path('productsApi/',products_api),
    path('productsApi/<int:id>',products_api),
    path('ClassBasedProductsApi/',ProductAPI.as_view()),
    path('ClassBasedProductsApi/<int:id>',ProductAPI.as_view()),
    path('ListProductAPI/',ListProductAPI.as_view()),
    # path('ListProductAPI/<int:pk>',RetrieveProductAPI.as_view()),
    # path('ListProductAPI/<int:pk>',UpdateProductAPI.as_view()),
    path('ListProductAPI/<int:pk>',DeleteProductAPI.as_view()),
    path('CreateProductAPI/',CreateProductAPI.as_view()),
    # path('GetPostProductAPI/',GetPostProductAPI.as_view()),
    # path('RetrievePutDeleteProductAPI/<int:pk>',RetrievePutDeleteProductAPI.as_view())
    path('GetPostProductAPI/',ProductListCreate.as_view()),
    path('RetrievePutDeleteProductAPI/<int:pk>',ProductRetrieveUpdateDestroy.as_view())
]
