from rest_framework import viewsets
from .models import *
from .serializers import *

# FinancialRecord ViewSet
class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer