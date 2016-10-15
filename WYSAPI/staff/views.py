from rest_framework import viewsets
from staff.models import Department,Jobs,EmpInfo
from staff.serializers import DepartmentSerializer,JobsSerializer,EmpInfoSerializer
# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.filter(deleted=None)
    serializer_class = DepartmentSerializer
    
class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.filter(deleted=None)
    serializer_class = JobsSerializer
    
class EmpInfoViewSet(viewsets.ModelViewSet):
    queryset = EmpInfo.objects.filter(deleted=None,user__is_active=True)
    serializer_class = EmpInfoSerializer
    