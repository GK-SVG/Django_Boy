from rest_framework import serializers
from .models import Employee

def start_with_a(data):
    if data[0].lower()!='a':
        raise serializers.ValidationError('Name should start with  A')
    return data


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[start_with_a])
    salery = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Employee.objects.create(**validate_data)
    

    def update(self,instance,validate_data):
        print(instance.name)
        instance.name = validate_data.get('name',instance.name)
        instance.salery = validate_data.get('salery',instance.salery)
        instance.city = validate_data.get('city',instance.city)
        print(instance.name)
        instance.save()
        return instance
    
    #Field level validation
    def validate_salery(self,value):
        if value>=50000:
            raise serializers.ValidationError("Salery can't be greater than 50000 in our company")
        return value
    
    #bject level validation
    def validate(self,data):
        salery = data.get('salery')
        city = data.get('city')
        if city.lower()!='alwar' or salery>=50000:
            raise serializers.ValidationError("Salery can't be greater than 50000 in our company OR city should be  Alwar")
        return data
