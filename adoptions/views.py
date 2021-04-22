from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import AdoptionSerializer
from .models import Adoption

# Create your views here.

class AdoptionListCreateAPIView(ListCreateAPIView):
    serializer_class = AdoptionSerializer
    queryset = Adoption.objects.all()