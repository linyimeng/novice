'''
Created on 2016-10-3

@author: yimeng
'''
from rest_framework import serializers
from goods.models import Type,TypeAttr,Goods

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('pk','name')
        
class TypeAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAttr
        fields= ('pk','goodstype','name','attr_type')
        
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields=('pk','name','customid','manufacturer','barcode','type','salesprice','costprice','is_active','main_attr',
                'custom_attr','other_attr','user','lastmodifyer')
        
        
        
    
    