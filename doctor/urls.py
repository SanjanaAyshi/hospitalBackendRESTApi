from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter() #this one is the router
router.register('Doctors', views.DoctorView) # this one is the antina
router.register('Specialization', views.SpecializationView) # this one is the antina
router.register('Availability', views.AvailabilityView) # this one is the antina
router.register('Designation', views.DesignationView) # this one is the antina
router.register('Review', views.ReviewView) # this one is the antina

urlpatterns = [
    path('', include(router.urls)),
]