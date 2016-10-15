from rest_framework import viewsets
from BP.models import Company
from BP.serializers import CompanySerializer
# Create your views here.

class VendorsViewSet(viewsets):
    queryset = Company.objects.filter(deleted=None,is_vendor=True)
    serializer_class = CompanySerializer
