from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializer

class ServiceView(viewsets.ModelViewSet):
    queryset=models.Services.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.ServicesSerializers

