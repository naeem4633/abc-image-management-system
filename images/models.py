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
    disease_type = models.CharField(max_length=255)  # New field for disease type
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
    images = models.ManyToManyField(MedicalImage, related_name='diagnoses')  # Linking to multiple medical images
    confirmed = models.BooleanField(default=False)  # Whether the diagnosis is confirmed
    confirmed_at = models.DateTimeField(null=True, blank=True)  # Time of confirmation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Diagnosis for {self.patient.user.username} by {self.staff.user.username} - {'Confirmed' if self.confirmed else 'Unconfirmed'}"

# Report Model
class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reports')
    images = models.ManyToManyField(MedicalImage, related_name='included_in_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    generated_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='reports_generated')

    def __str__(self):
        return f"Report for {self.patient.user.username} on {self.created_at}"
    
# Task Model
class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    task_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='tasks')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='tasks')
    task_type = models.CharField(max_length=255)  # e.g., upload image, generate diagnosis, consultation
    image = models.ForeignKey(MedicalImage, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Task {self.task_id} for {self.patient.user.username} by {self.staff.user.username}"


# StaffTask Model
class StaffTask(models.Model):
    staff_task_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_tasks')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='staff_tasks')
    role = models.CharField(max_length=255)  # e.g., diagnosing, reviewing
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"StaffTask {self.staff_task_id} for {self.task} by {self.staff.user.username}"