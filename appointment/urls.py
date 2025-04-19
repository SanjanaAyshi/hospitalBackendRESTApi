from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter() #this one is the router
router.register('', views.AppointmentView) # this one is the antina

urlpatterns = [
    path('', include(router.urls)),
]