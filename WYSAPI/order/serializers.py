'''
Created on 2016-10-5

@author: yimeng
'''
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from order.models import Type,Order
from goods.models import Goods
from staff.models import EmpInfo

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ('name','io')
        
        
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
                   'ordercode',
                   'company',
                   'type',
                   'totalquantity',
                   'totalprice',
                   'remark',
                   'creator'
                 )

