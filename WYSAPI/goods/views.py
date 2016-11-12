from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from goods.models import Type,TypeAttr,Goods
from goods.serializers import TypeSerializer,TypeAttrSerializer,GoodsSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.filter()
    serializer_class = TypeSerializer

class TypeAttrCreateAPIView(CreateAPIView):
    serializer_class = TypeAttrSerializer
    
class TypeAttrListAPIView(ListAPIView):
    '''
    商品属性查询
        商品属性分为静态属性(s),动态属性(d)
    '''
    serializer_class = TypeAttrSerializer
    def get_queryset(self,*args,**kwargs):
        goodstype = self.kwargs['gtid']
        attrtype = self.kwargs.get('type',None)
        if attrtype is None:
            queryset_list = TypeAttr.objects.filter(goodstype__id__in=[goodstype,0])
        else:
            if attrtype == 's':
                type_set = TypeAttr.objects.filter(type='ss')
            elif attrtype == 'd':
                type_set = TypeAttr.objects.filter(type='sd')
            else:
                return TypeAttr.objects.filter(goodstype__id=goodstype,type=attrtype)
            queryset_list = TypeAttr.objects.filter(goodstype__id=goodstype,type=attrtype) | type_set
        return queryset_list
    
class TypeAttrRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TypeAttr.objects.all()
    serializer_class = TypeAttrSerializer
    lookup_field = 'keyname'

class GoodsViewSet(ModelViewSet):
    queryset = Goods.objects.filter()
    serializer_class = GoodsSerializer
# class GoodsSearchListAPIView(ListAPIView):
#     queryset = Goods.objects.filter()
#     serializer_class = GoodsSearchSerializer
#     filter_backends = [SearchFilter,OrderingFilter]
#     search_fields = ['name','barcode']
#     