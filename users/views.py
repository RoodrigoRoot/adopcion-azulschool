from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from  .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()