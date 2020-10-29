from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def SetCookie(request):
    response = render(request,'setCookies.html')
    response.set_cookie('name','gautam',expires=datetime.utcnow()+timedelta(days=4))
    return response


def GetCookie(request):
    #name = request.COOKIES['name']
    name = request.COOKIES.get('name','Guest')
    return render(request,'getCookies.html',{'name':name})
    

def DelCookie(request):
    response = render(request,'delCookies.html')
    response.delete_cookie('name')
    return response
     