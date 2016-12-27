from rest_framework import viewsets
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,ListAPIView,RetrieveAPIView
from staff.models import Department,Jobs,EmpInfo
from staff.serializers import DepartmentSerializer,JobsSerializer,EmpInfoCreateSerializer,EmpInfoListDetailSerializer
from staff.pagination import StaffLimitOffsetPagination
# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer
    #默认引用系统分页，可以定制自己的分页
    pagination_class = StaffLimitOffsetPagination

class JobsListAPIView(ListAPIView):
    serializer_class = JobsSerializer
    def get_queryset(self,*args,**kwargs):
        dpk = self.kwargs['dpk']
        queryset_list = Jobs.objects.filter(department__pk=dpk)
        return queryset_list
    
class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.filter()
    serializer_class = JobsSerializer
    
class EmpInfoCreateAPIView(CreateAPIView):
    serializer_class = EmpInfoCreateSerializer
    
class EmpInfoListAPIView(ListAPIView):
    pagination_class = StaffLimitOffsetPagination
    queryset = EmpInfo.objects.filter(user__is_active=True)
    serializer_class = EmpInfoListDetailSerializer
class EmpInfoRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = EmpInfo.objects.filter(user__is_active=True)
    serializer_class = EmpInfoListDetailSerializer
    
class EmpInfoRetrieveAPIView(RetrieveAPIView):
    queryset = EmpInfo.objects.filter(user__is_active=True)
    serializer_class = EmpInfoListDetailSerializer
    lookup_field = 'user'