from django.core.management.base import BaseCommand
from accounts.models import Patient, Staff
from images.models import MedicalImage, Diagnosis, Report
import random

class Command(BaseCommand):
    help = 'Seed images and reports data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding images...')

        # Create Medical Images
        image_types = ['MRI', 'CT', 'XRay']
        for i in range(20):
            MedicalImage.objects.create(
                patient=Patient.objects.order_by('?').first(),
                image_type=random.choice(image_types),
                image_url=f'https://example.com/image_{i}.jpg',
                cost=random.uniform(100, 1000)
            )

        # Create Diagnoses
        for i in range(15):
            Diagnosis.objects.create(
                patient=Patient.objects.order_by('?').first(),
                staff=Staff.objects.order_by('?').first(),
                diagnosis_details=f'Diagnosis details for patient {i}.'
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded images and diagnoses data!'))

        # Create Reports
        self.stdout.write('Seeding reports...')
        for i in range(10):
            patient = Patient.objects.order_by('?').first()
            images = MedicalImage.objects.filter(patient=patient)[:3]  # Get up to 3 random images for the patient
            staff = Staff.objects.order_by('?').first()

            if images:
                report = Report.objects.create(
                    patient=patient,
                    generated_by=staff
                )
                report.images.set(images)  # Add images to the report
                report.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded reports!'))
