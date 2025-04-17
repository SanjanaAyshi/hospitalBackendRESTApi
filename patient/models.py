from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    users=models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber=models.CharField(max_length=12)
    image=models.ImageField(upload_to='patient/image/')

    def __str__(self):
        return f"{self.users.first_name} {self.users.last_name}"
    