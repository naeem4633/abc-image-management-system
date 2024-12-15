from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalImageViewSet, DiagnosisViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'medical-images', MedicalImageViewSet, basename='medicalimage')
router.register(r'diagnoses', DiagnosisViewSet, basename='diagnosis')
router.register(r'reports', ReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),
]