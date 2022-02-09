from urllib import request

from django.shortcuts import render
from . models import Users,Teams
from .serializers import UserSerializer,TeamSerializer
from rest_framework import generics

# Create your views here.

class user_objects(generics.ListCreateAPIView):
    queryset = Users.objects.filter(is_active=True)
    serializer_class = UserSerializer

class user_objects_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class team_objects(generics.ListCreateAPIView):
    queryset = Teams.objects.filter(is_active=True)
    serializer_class = TeamSerializer

class team_objects_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teams.objects.filter(is_active=True)
    serializer_class = TeamSerializer