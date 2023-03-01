from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class PersonaView(viewsets.ModelViewSet):
    
    serializer_class = PersonaSerializers

    queryset = Personas.objects.all()