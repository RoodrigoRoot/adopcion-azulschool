from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Pet
from .serializers import PetSerializer

# Create your views here.

class PetsListCreateAPIView(ListCreateAPIView):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()