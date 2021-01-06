from django.shortcuts import render
from .serializers import EmployeeSerializer
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Employee


def employee_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")