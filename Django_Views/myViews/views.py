from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
#-----------------Functional View----------------------
def func(request):
    return HttpResponse('This is function based view')


#-----------------Class Based View---------------------

class ClassView(View):
    def get(self,request):
        return HttpResponse('This is Class based view')