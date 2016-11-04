'''
Created on 2016-11-3

@author: yimeng
'''
from rest_framework.serializers import ModelSerializer,DateTimeField,SerializerMethodField
from order.models import Type,Order,Detail
from BP.models import Company

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ('name','io')
        
class DetailSerializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = ('order','goods','quantity',
                  'price','dynamic_attr','remark')
    
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
        return obj.company.name
    
    def get_type(self,obj):
        return obj.type.name
    
    def get_creator(self,obj):
        return obj.creator.name
        
        
        
        
        
        
        
        