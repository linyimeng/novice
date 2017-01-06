from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from partner.models import Company,Personal
from partner.serializers import CompanySerializer,PersonalSerializer

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(('GET',))
def api_root(request,format=None):
    return Response({
        '单位列表(按供应商，客户类型提取)':reverse('company-list',request=request,args=('I'),format=format),
        '单位详情':reverse('company-detail',request=request,args=('1',),format=format),
        '创建单位':reverse('company-create',request=request,format=format),
    })

class CompanyCreateAPIView(CreateAPIView):
    serializer_class = CompanySerializer
class CompanyListAPIView(ListAPIView):
    '''
    按类型提取公司列表
    '''
    #queryset = Company.objects.filter(deleted=None)
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        companytype = self.kwargs['companytype']
        if companytype=='vendor':
            queryset_list = Company.objects.filter(deleted=None,is_vendor=True)
        elif companytype=='client':
            queryset_list = Company.objects.filter(deleted=None,is_client=True)
        elif companytype=="vc":
            queryset_list = Company.objects.filter(deleted=None,is_vendor=True,is_client=True)
        else:
            queryset_list = []
        return queryset_list
class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.filter(deleted=None)
    serializer_class = CompanySerializer
    
class PersonalViewSet(ModelViewSet):
    queryset = Personal.objects.filter(deleted=None)
    serializer_class = PersonalSerializer
