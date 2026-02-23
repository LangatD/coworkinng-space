from django.shortcuts import render
from rest_framework import viewsets
from .models import CoworkingSpace
from .serializers import CoworkingSpaceSerializer

class CoworkingSpaceViewSet(viewsets.ModelViewSet):
    queryset = CoworkingSpace.objects.all()
    serializer_class = CoworkingSpaceSerializer