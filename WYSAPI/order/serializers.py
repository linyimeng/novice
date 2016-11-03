'''
Created on 2016-11-3

@author: yimeng
'''
from rest_framework.serializers import ModelSerializer
from order.models import Type,Order,Detail

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ('name','io')
        
class DetailSerializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = ('order','goods','quantity','price','dynamic_attr','remark')
    
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
                  'creator'
                 )
    