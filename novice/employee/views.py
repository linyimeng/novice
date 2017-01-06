from rest_framework import viewsets
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,ListAPIView,RetrieveAPIView
from employee.models import Department,Jobs,EmpInfo
from employee.serializers import DepartmentSerializer,JobsSerializer,EmpInfoCreateSerializer,EmpInfoListDetailSerializer
from employee.pagination import StaffLimitOffsetPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(('GET',))
def api_root(request,format=None):
    return Response({
        '员工列表':reverse('emps-list',request=request,format=format),
        '创建员工':reverse('emps-create',request=request,format=format),
        '员工详情':reverse('emps-detail',request=request,args=('1',),format=format),
    })

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