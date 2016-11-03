from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from BP.models import Company,Personal
from BP.serializers import CompanySerializer,PersonalSerializer
# Create your views here.
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
