from rest_framework import serializers, viewsets
from .models import Patient, FinancialRecord

# FinancialRecord Serializer
class FinancialRecordSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = FinancialRecord
        fields = ['__all__']