from rest_framework import serializers
from . import models

class DoctorSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    availableTime = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    
    class Meta:
        model=models.Doctor
        fields='__all__'
class SpecializationSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Specialization
        fields='__all__'
class AvailabilitySerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Availability
        fields='__all__'
class DesignationSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Designation
        fields='__all__'
class ReviewSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Review
        fields='__all__'