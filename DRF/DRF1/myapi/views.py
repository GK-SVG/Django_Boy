from django.shortcuts import render,HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
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
