from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializer

class AppointmentView(viewsets.ModelViewSet):
    queryset=models.Appointment.objects.all()  # sob prokar query korte parbe
    serializer_class=serializer.AppointmentSerializers


    def get_queryset(self):
        querySet= super().get_queryset()
        patientId=self.request.query_params.get('patientId')
        if patientId:
            querySet=querySet.filter(patientId=patientId)
            return querySet