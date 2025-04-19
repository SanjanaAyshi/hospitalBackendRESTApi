from django.db import models
from patient.models import Patient
from doctor.models import Doctor, Availability
# Create your models here.

AppointmentStatus = [
    ("Completed", "Completed"),
    ("Pending", "Pending"),
    ("Canceled", "Canceled"),
]

AppointmentType = [
    ("Online", "Online"),
    ("Offline", "Offline"),
]


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointmentStatus= models.CharField(choices=AppointmentStatus, max_length=20, default='Pending')
    appointmentType=models.CharField(choices= AppointmentType, max_length=20)
    symptom=models.TextField()
    time=models.ForeignKey(Availability, on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name}, Patient: {self.patient.users.first_name}"
