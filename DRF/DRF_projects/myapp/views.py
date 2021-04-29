from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    return Response(data="You are logged in",status=status.HTTP_200_OK)