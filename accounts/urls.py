from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, PatientViewSet, StaffViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'staff', StaffViewSet, basename='staff')

urlpatterns = [
    path('', include(router.urls)),
]