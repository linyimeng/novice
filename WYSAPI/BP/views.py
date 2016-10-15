from rest_framework import viewsets
from BP.models import Company,Personal
from BP.serializers import CompanySerializer,PersonalSerializer
# Create your views here.

class CompanyViewSet(viewsets):
    queryset = Company.objects.filter(deleted=None)
    serializer_class = CompanySerializer
    
class PersonalViewSet(viewsets):
    queryset = Personal.objects.filter(deleted=None)
    serializer_class = PersonalSerializer
