from rest_framework import serializers, viewsets
from .models import *

# CustomUser Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['__all__']

# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Patient
        fields = ['__all__']

# Staff Serializer
class StaffSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Staff
        fields = ['__all__']