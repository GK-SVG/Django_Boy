from django.shortcuts import render

# Create your views here.
def mycache(request):
    return render(request,'cache.html')