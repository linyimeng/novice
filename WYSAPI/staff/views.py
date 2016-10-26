from rest_framework import viewsets
from staff.models import Department,Jobs,EmpInfo
from staff.serializers import DepartmentSerializer,JobsSerializer,EmpInfoSerializer
from staff.pagination import StaffLimitOffsetPagination
# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer
    #默认引用系统分页，可以定制自己的分页
    pagination_class = StaffLimitOffsetPagination
    
class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.filter()
    serializer_class = JobsSerializer
    
class EmpInfoViewSet(viewsets.ModelViewSet):
    queryset = EmpInfo.objects.filter(user__is_active=True)
    serializer_class = EmpInfoSerializer
    pagination_class = StaffLimitOffsetPagination