'''
Created on 2016-10-3

@author: yimeng
'''
from rest_framework import serializers
from goods.models import Type,TypeAttr,Goods

class TypeSerializer(serializers.ModelSerializer):
    superiors_name = serializers.SerializerMethodField()
    class Meta:
        model = Type
        fields = ('pk','name','superiors','superiors_name')
    
    def get_superiors_name(self,obj):
        if obj.superiors:
            return obj.superiors.name
        return None
    
class TypeAttrSerializer(serializers.ModelSerializer):
    goodstype = serializers.IntegerField(write_only=True)
    class Meta:
        model = TypeAttr
        fields= ('goodstype','logicname','name','attr_type')
        
        
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields=(
                'pk',
                'name',
                'customid',
                'manufacturer',
                'specification',
                'unit',
                'barcode',
                'type',
                'salesprice',
                'costprice',
                'is_active',
                'static_attr',
                'user',
                'lastmodifyer'
                )