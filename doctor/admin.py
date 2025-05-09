from django.contrib import admin
from . import models
# Register your models here.

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("Title",)} 
admin.site.register(models.Specialization,SpecializationAdmin)
admin.site.register(models.Availability)
admin.site.register(models.Designation,DesignationAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)
