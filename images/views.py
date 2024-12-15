from rest_framework import viewsets
from .models import MedicalImage, Diagnosis, Report
from .serializers import * 

# MedicalImage ViewSet
class MedicalImageViewSet(viewsets.ModelViewSet):
    queryset = MedicalImage.objects.all()
    serializer_class = MedicalImageSerializer

# Diagnosis ViewSet
class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

# Report ViewSet
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer