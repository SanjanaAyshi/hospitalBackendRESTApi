from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializer

class PatientView(viewsets.ModelViewSet):
    queryset=models.Patient.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.PatientSerializers