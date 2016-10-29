from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from goods.models import Type,TypeAttr,Goods
from goods.serializers import TypeSerializer,TypeAttrSerializer,GoodsSerializer
# Create your views here.

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.filter()
    serializer_class = TypeSerializer

class TypeAttrListCreateAPIView(ListCreateAPIView):
    serializer_class = TypeAttrSerializer
    def get_queryset(self,*args,**kwargs):
        goodstype = self.kwargs['tid']
        attrtype = self.kwargs['attrtype']
        queryset_list = TypeAttr.objects.filter(goodstype__id=goodstype,attr_type=attrtype)
        return queryset_list
        
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