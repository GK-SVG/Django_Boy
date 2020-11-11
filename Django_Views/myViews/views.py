from django.shortcuts import render,HttpResponse
from .forms import Contact
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.
#-----------------Functional View----------------------
def func(request):
    return HttpResponse('This is function based view')


#-----------------Class Based View---------------------

class ClassView(View):
    def get(self,request):
        return HttpResponse('This is Class based view')


#------------------------Post Request Based Function----------------
def contact(request):
    if request.method == "POST":
        number = Contact(request.POST)
        if number.is_valid():
            return HttpResponse("form submited")
    else:
        form = Contact()
        return render(request,'contact.html',{'form':form})


#------------------------Post Request Based Class----------------
class ClassContact(View):
    def get(self,request):
        form = Contact()
        return render(request,'contact.html',{'form':form})
        
    def post(self,request):
        number = Contact(request.POST)
        if number.is_valid():
            return HttpResponse("form submited")

#---------------------------One function based view called by 2 URLS--------------
def fun(request,template_name):
    template_name = template_name
    return render(request,template_name,{'name':"Gautam"})
        

#------------One Class based view called by 2 URLS--------------------------------
class MyclassView(View):
    template_name = ''
    def get(self,request):
        return render(request,self.template_name,{'name':"Gautam"})



#---------Django Template Class Based view
class IndexTemplateView(TemplateView):
    template_name = 'class1.html'


class Index2Template(TemplateView):
    template_name = "class1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Gautam" 
        return context
    