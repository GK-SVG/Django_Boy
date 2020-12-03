from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers


def index(request):
    if request.is_ajax and request.method == "POST":
        print('number==',request.POST['phone'])
        return JsonResponse({"instance": "number submited"}, status=200)
    return render(request,'mni/index.html')