from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.
class Specialization(models.Model):
    name=models.CharField( max_length=50)
    slug=models.CharField( max_length=50)
    def __str__(self):
        return self.name
    
class Availability(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name
    
class Designation(models.Model):
    Title=models.CharField( max_length=50)
    slug=models.CharField( max_length=50)
    def __str__(self):
        return self.Title

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='doctor/image/')
    designation=models.ManyToManyField(Designation)
    availableTime=models.ForeignKey(Availability, on_delete=models.CASCADE)
    specialization=models.ManyToManyField(Specialization)
    fee=models.IntegerField()
    meetLink=models.CharField( max_length=18)

    def __str__(self):
        return f"Dr.{self.user.first_name}{self.user.last_name}"

StarChoices = [
    ("⭐", "⭐"),
    ("⭐⭐", "⭐⭐"),
    ("⭐⭐⭐", "⭐⭐⭐"),
    ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
]


class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    ratings = models.CharField(choices=StarChoices, max_length=10)

    def __str__(self):
        return f"Patient: {self.reviewer.users.first_name} {self.reviewer.users.last_name}, Doctor: {self.doctor.user.first_name}"
