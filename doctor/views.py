from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializer

class DoctorView(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.DoctorSerializers
class SpecializationView(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.SpecializationSerializers
class AvailabilityView(viewsets.ModelViewSet):
    queryset=models.Availability.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.AvailabilitySerializers
class DesignationView(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.DesignationSerializers
class ReviewView(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.ReviewSerializers