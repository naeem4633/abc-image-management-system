from django.db import models
from accounts.models import *

# FinancialRecord Model
class FinancialRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='financial_records')
    description = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - {self.cost} for {self.patient.user.username}"