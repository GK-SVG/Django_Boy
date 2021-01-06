from rest_framework import serializers
from .models import Employee



class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    salery = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Employee.objects.create(**validate_data)
    

    def update(self,instance,validate_data):
        print(instance)
        instance.name = validate_data.get('name',instance.name)
        instance.salery = validate_data.get('salery',instance.salery)
        instance.city = validate_data.get('city',instance.city)
        print(instance)
        instance.save()
        return instance