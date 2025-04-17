from django.db import models

# Create your models here.
class Services(models.Model):
    name=models.CharField(max_length=20)
    describtion=models.TextField()
    image=models.ImageField(upload_to="service/image/")

    class Meta:
        verbose_name_plural = 'Services'