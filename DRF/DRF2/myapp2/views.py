from django.shortcuts import render
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt,name="dispatch")
class StudentAPI(View):
    def get(self,request,*args, **kwargs):
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser().parse(stream)
        # id = python_data.get('id',None)
        # if id is not None:
        #     stu = Student.objects.get(id=id)
        #     serializer = StudentSerializer(stu)
        #     json_data = JSONRenderer().render(serializer.data)
        #     return HttpResponse(json_data,content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")
    def post(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            resp = {'Success':'Data Created Successfully'}
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data,content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                resp = {'Success':'Data Updated Successfully'}
                json_data = JSONRenderer().render(resp)
                return HttpResponse(json_data,content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            stu.delete()
            resp = {'Success':'Data Deleted Successfully'}
            # json_data = JSONRenderer().render(resp)
            # return HttpResponse(json_data,content_type="application/json")
            return JsonResponse(resp,safe=False)
