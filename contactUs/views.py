from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializaer

class ContactUsView(viewsets.ModelViewSet):
    queryset=models.ContactUs.objects.all() # sob prokar query korte parbe
    serializer_class=serializaer.ContactUsSerializers 
    