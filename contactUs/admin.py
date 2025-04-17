from django.contrib import admin
from .models import ContactUs
# Register your models here.

class CreateModelAdmin(admin.ModelAdmin):
    list_display=["name",'phoneNumber', 'problem']
admin.site.register(ContactUs, CreateModelAdmin)