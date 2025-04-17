from django.contrib import admin
from . import models

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['DoctorName', 'PatientName', 'appointmentStatus', 'appointmentType', 'symptom', 'time', 'cancel']

    def PatientName(self, obj):
        return obj.patient.users.first_name

    def DoctorName(self, obj):
        return obj.doctor.user.first_name

admin.site.register(models.Appointment, AppointmentAdmin)
