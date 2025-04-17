from django.contrib import admin
from . import models
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display=['getFirstName','getLastName','phoneNumber', 'image']

    def getFirstName(self,obj):
        return obj.users.first_name
    def getLastName(self,obj):
        return obj.users.last_name

admin.site.register(models.Patient,PatientAdmin)