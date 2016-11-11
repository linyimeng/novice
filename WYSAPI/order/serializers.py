'''
Created on 2016-11-3

@author: yimeng
'''
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from order.models import Type,Order,Detail
from goods.serializers import GoodsSerializer
class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ('name','io')
        
class DetailSerializer(ModelSerializer):
    name = SerializerMethodField()
    manufacturer = SerializerMethodField()
    specification = SerializerMethodField()
    company = SerializerMethodField()
    class Meta:
        model = Detail
        fields = ('order','goods','name','manufacturer','specification','quantity',
                  'price','productiondate','validity','batch','dynamic_attr','remark','joined','company')
        
    def get_name(self,obj):
        return obj.goods.name

    
    def get_specification(self,obj):
        return obj.goods.specification
    
    def get_manufacturer(self,obj):
        return obj.goods.manufacturer
    
    def get_company(self,obj):
        if obj.order.company:
            return obj.order.company.name
        return None
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
                  'ordercode',
                  'totalquantity',
                  'totalprice',
                  'company',
                  'type',
                  'remark',
                  'creator',
                 )

class OrderListSerializer(ModelSerializer):
    company = SerializerMethodField()
    type = SerializerMethodField()
    creator = SerializerMethodField()
    class Meta:
        model = Order
        fields = (
                  'ordercode',
                  'totalquantity',
                  'totalprice',
                  'joined',
                  'company',
                  'type',
                  'remark',
                  'creator'
                 )
    def get_company(self,obj):
        if obj.company:
            return obj.company.name
        return None
    
    def get_type(self,obj):
        return obj.type.name
    
    def get_creator(self,obj):
        return obj.creator.name
    
class DetailRetrieveSerializer(ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = Detail
        fields = ('order','goods','quantity','productiondate','validity','batch',
                  'price','dynamic_attr','remark')
    
class OrderRetrieveSerializer(ModelSerializer):
    company = SerializerMethodField()
    type = SerializerMethodField()
    creator = SerializerMethodField()
    detail = SerializerMethodField()
    class Meta:
        model = Order
        fields = (
                  'ordercode',
                  'totalquantity',
                  'totalprice',
                  'joined',
                  'company',
                  'type',
                  'remark',
                  'creator',
                  'detail'
                 )
    def get_company(self,obj):
        return obj.company.name
    
    def get_type(self,obj):
        return obj.type.name
    
    def get_creator(self,obj):
        return obj.creator.name

    def get_detail(self,obj):
        detail_set = Detail.objects.filter(order__pk=obj.ordercode)
        detail = DetailRetrieveSerializer(detail_set,many=True).data
        return detail
    
        
        
        
        
        
        
        
        