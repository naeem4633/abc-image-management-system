from django.core.management.base import BaseCommand
from accounts.models import CustomUser, Patient, Staff
import random

class Command(BaseCommand):
    help = 'Seed accounts app data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding accounts...')

        # Create Admin User
        CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            role='admin'
        )

        # Create Patients
        for i in range(10):
            user = CustomUser.objects.create_user(
                username=f'patient{i}',
                email=f'patient{i}@example.com',
                password='password123',
                role='patient'
            )
            Patient.objects.create(user=user, medical_history='No significant history.')

        # Create Staff
        specializations = ['Radiologist', 'Oncologist', 'Cardiologist']
        for i in range(5):
            user = CustomUser.objects.create_user(
                username=f'staff{i}',
                email=f'staff{i}@example.com',
                password='password123',
                role='staff'
            )
            Staff.objects.create(user=user, specialization=random.choice(specializations))

        self.stdout.write(self.style.SUCCESS('Successfully seeded accounts data!'))
