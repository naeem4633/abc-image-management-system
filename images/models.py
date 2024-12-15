from django.db import models
from accounts.models import *

# MedicalImage Model
class MedicalImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('MRI', 'MRI'),
        ('CT', 'CT'),
        ('XRay', 'XRay'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='images')
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPE_CHOICES)
    upload_date = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=255)  # Changed ImageField to CharField
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.image_type} for {self.patient.user.username} - {self.upload_date}"

# Diagnosis Model
class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnoses')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='diagnoses_made')
    diagnosis_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Diagnosis for {self.patient.user.username} by {self.staff.user.username}"

# Report Model
class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reports')
    images = models.ManyToManyField(MedicalImage, related_name='included_in_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    generated_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='reports_generated')

    def __str__(self):
        return f"Report for {self.patient.user.username} on {self.created_at}"