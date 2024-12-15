from rest_framework import serializers, viewsets
from .models import *

# MedicalImage Serializer
class MedicalImageSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = MedicalImage
        fields = '__all__'

# Diagnosis Serializer
class DiagnosisSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    staff = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())

    class Meta:
        model = Diagnosis
        fields = '__all__'

# Report Serializer
class ReportSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=MedicalImage.objects.all())
    generated_by = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())

    class Meta:
        model = Report
        fields = '__all__'