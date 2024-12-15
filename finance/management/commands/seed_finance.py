from django.core.management.base import BaseCommand
from accounts.models import Patient
from finance.models import FinancialRecord
import random

class Command(BaseCommand):
    help = 'Seed finance app data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding finance...')

        # Create Financial Records
        for i in range(15):
            FinancialRecord.objects.create(
                patient=Patient.objects.order_by('?').first(),
                description=f'Service {i} payment',
                cost=random.uniform(50, 500)
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded finance data!'))
