from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

def students_details(request,pk):
    stu = Student.objects.get(id=pk)
    print('stu obj',stu)
    serializer = StudentSerializer(stu)
    print('serialized/native python data',serializer)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)



def students(request):
    stu = Student.objects.all()
    print('stu obj',stu)
    serializer = StudentSerializer(stu,many=True)
    print('serialized/native python data',serializer)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def create_Stu(request):
    if request.method=="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data =  JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data Craeted'}
            # json_data = JSONRenderer().render(response)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(response)
        response = serializer.errors
        return JsonResponse(response)
        