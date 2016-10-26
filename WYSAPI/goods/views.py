from rest_framework.viewsets import ModelViewSet
from goods.models import Type,TypeAttr,Goods
from goods.serializers import TypeSerializer,TypeAttrSerializer,GoodsSerializer
# Create your views here.

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.filter()
    serializer_class = TypeSerializer
    
class TypeAttrViewSet(ModelViewSet):
    queryset = TypeAttr.objects.filter()
    serializer_class = TypeAttrSerializer

class GoodsViewSet(ModelViewSet):
    '''
    main_attr: json string {"attrname":"attrvalue"}
    custom_attr: json string {"attrname":"attrvalue"}
    other_attr: json string {"attrname":"attrvalue"}
    '''
    queryset = Goods.objects.filter(is_active=True)
    serializer_class = GoodsSerializer