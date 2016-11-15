from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,ListCreateAPIView
from goods.models import Type,TypeAttr,Goods
from goods.serializers import TypeSerializer,TypeAttrSerializer,GoodsCreateUpdateSerializer,GoodsListSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
# from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
@api_view(('GET',))
def api_root(request,format=None):
    return Response({
        '商品列表和创建':reverse('goods-list',request=request, format=format),
        '商品详情及更新':reverse('goods-detail',request=request,args=('2',),format=format),
        '属性创建':reverse('typeattr-create',request=request,format=format),
        '属性详情':reverse('goodsattr-detail',request=request,args=('saleprice',),format=format),
        '获取商品静态属性和动态属性列表':reverse('goodsattr-all-list',request=request,args=('1',),format=format),
        '商品指定列别属性列表':reverse('goodsattr-list',request=request,args=('1','s'),format=format),
        '商品类型列表，创建，详情':'http://127.0.0.1:8000/api/goods/type/',
    })
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

class GoodsListCreateAPIView(ListCreateAPIView):
    queryset = Goods.objects.filter(gsav__is_active=True)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = GoodsCreateUpdateSerializer
        else:
            self.serializer_class = GoodsListSerializer
        return self.serializer_class
    
class GoodsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.filter(gsav__is_active=True)
    def get_serializer_class(self):
        if self.request.method == 'PUT' or 'PETCH':
            self.serializer_class = GoodsCreateUpdateSerializer
        else:
            self.serializer_class = GoodsListSerializer
        return self.serializer_class

# class GoodsSearchListAPIView(ListAPIView):
#     queryset = Goods.objects.filter()
#     serializer_class = GoodsSearchSerializer
#     filter_backends = [SearchFilter,OrderingFilter]
#     search_fields = ['name','barcode']