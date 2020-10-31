from django.shortcuts import render
from datetime import datetime, timedelta
from .models import StudentData
# Create your views here.
def SetCookie(request):
    students = StudentData.objects.all()
    response = render(request,'setCookies.html',{'students':students})
    # temp_stu = []
    # for student in students:
    #     temp_stu.append(student.name)
    response.set_cookie('students',students,expires=datetime.utcnow()+timedelta(days=4))
    return response


def GetCookie(request):
    #name = request.COOKIES['name']
    name = request.COOKIES.get('students','Guest')
    # name=name.replace('[','')
    # name=name.replace(']','')
    # name=name.replace("'",'')
    # name=name.replace(",",'')
    
    # print(name)
    return render(request,'getCookies.html',{'name':name})
    

def DelCookie(request):
    response = render(request,'delCookies.html')
    response.delete_cookie('name')
    return response
     