from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

@login_required(login_url="Login")
def home(request):
    pass

