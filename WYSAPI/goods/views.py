from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from goods.models import Type,TypeAttr,Goods
from goods.serializers import TypeSerializer,TypeAttrSerializer,GoodsSerializer,GoodsSearchSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.filter()
    serializer_class = TypeSerializer

class TypeAttrListAPIView(ListAPIView):
    serializer_class = TypeAttrSerializer
    def get_queryset(self,*args,**kwargs):
        #goodstype = self.kwargs['tid']
        goodstype = 1
        attrtype = self.kwargs['attrtype']
        queryset_list = TypeAttr.objects.filter(goodstype__id=goodstype,attr_type=attrtype)
        return queryset_list

class TypeAttrCreateAPIView(CreateAPIView):
    serializer_class = TypeAttrSerializer
        
class TypeAttrRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TypeAttr.objects.all()
    serializer_class = TypeAttrSerializer

class GoodsViewSet(ModelViewSet):
    '''
    main_attr: json string {"attrname":"attrvalue"}
    custom_attr: json string {"attrname":"attrvalue"}
    other_attr: json string {"attrname":"attrvalue"}
    '''
    queryset = Goods.objects.filter(is_active=True)
    serializer_class = GoodsSerializer

class GoodsSearchListAPIView(ListAPIView):
    queryset = Goods.objects.filter(is_active=True)
    serializer_class = GoodsSearchSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','barcode']
    