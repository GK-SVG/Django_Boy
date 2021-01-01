from django.shortcuts import render
from websites.models import Website

def home_view(request):
    name = "Welcome to"

    obj = Website.objects.get(id=1)

    context = {
        'name': name,
        'obj' : obj,
    }

    return render(request, 'home.html', context)