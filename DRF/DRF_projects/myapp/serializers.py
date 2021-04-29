from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from .models import *

class UserCreatingSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','username','password','phone','first_name','last_name')