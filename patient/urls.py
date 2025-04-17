from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter() #this one is the router
router.register('list', views.PatientView) # this one is the antina

urlpatterns = [
    path('', include(router.urls)),
]