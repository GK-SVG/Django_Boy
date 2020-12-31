from django.shortcuts import render,HttpResponse
from myapp.models import Profile


def index(request,code):
    try:
        profile = Profile.objects.get(code=code)
        return render(request,"index.html",{'profile':profile})
    except:
        return HttpResponse("Reffrel Code Does not Exist")
