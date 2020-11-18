"""Django_Views URL Configuration

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
from myViews.views import (func,ClassView,contact,ClassContact,EmpView,
                            fun,MyclassView,IndexTemplateView,
                            SiteRedirectView,EmpDetailView)
from django.views.generic.base import TemplateView,RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/',func,name="func"),
    path('cls/',ClassView.as_view(),name="cls"),
    path('confunc/',contact),
    path('clscont/',ClassContact.as_view()),
    path('fun1/',fun,{'template_name':"class1.html"},name="fun1"),
    path('fun2/',fun,{'template_name':"class2.html"},name="fun2"),
    path('cls1/',MyclassView.as_view(template_name="class1.html")),
    path('cls2/',MyclassView.as_view(template_name="class2.html")),
    path('index/',IndexTemplateView.as_view(extra_context={'roll':101}),name="index"),
    path('home/',RedirectView.as_view(url="/index/")),
    path('home2/',SiteRedirectView.as_view(),name="home2"),
    path('home3/',SiteRedirectView.as_view(pattern_name='home2')),
    path('',EmpView.as_view()),
    path('emp/<int:pk>',EmpDetailView.as_view())

]
