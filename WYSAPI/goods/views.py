from rest_framework import viewsets
from goods.models import Type,TypeAttr,Goods
from goods.serializers import TypeSerializer,TypeAttrSerializer,GoodsSerializer
# Create your views here.

class TypeViewSet(viewsets):
    queryset = Type.objects.filter(deleted=None)
    serializer_class = TypeSerializer
    
class TypeAttrViewSet(viewsets):
    queryset = TypeAttr.objects.filter(deleted=None)
    serializer_class = TypeAttrSerializer

class GoodsViewSet(viewsets):
    '''
    main_attr: json string {"attrname":"attrvalue"}
    custom_attr: json string {"attrname":"attrvalue"}
    other_attr: json string {"attrname":"attrvalue"}
    '''
    queryset = Goods.objects.filter(deleted=None,is_active=True)
    serializer_class = GoodsSerializer