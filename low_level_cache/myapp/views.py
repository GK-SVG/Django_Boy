from django.shortcuts import render
from django.core.cache import cache
from .models import StudentData

# Create your views here.
# def home(request):
#     mv = cache.get('movie','has_expired')
#     if mv=='has_expired':
#         cache.set('movie','the one', 60)
#         mv=cache.get('movie')
#     return render(request,'cache.html',{'movie':mv})


# def home(request):
#     mv = cache.get_or_set('name','The Manjhi',30)
#     return render(request,'cache.html',{'movie':mv})


# def home(request):
#     data = {'name':['gk','uk'],'roll':[1,2]}
#     cache.set_many(data,60)
#     dt = cache.get_many(data)
#     name= dt['name']
#     roll= dt['roll']
#     print(name)
#     print(roll)
#     return render(request,'cache.html',{'name':name,'roll':roll})

def home(request):
    stu = StudentData.objects.all()
    cache.set('students',stu,300)
    data = cache.get('students')
    print(data)
    return render(request,'cache.html',{'stu':data})

# def home(request):
#     data = [{'name':'gk','roll':2},{'name':'uk','roll':1}]
#     print('data====',data)
#     cache.set_many(data,60)
#     dt = cache.get_many(data)
#     print('dt====',dt)
#     return render(request,'cache.html',{'data':dt})

