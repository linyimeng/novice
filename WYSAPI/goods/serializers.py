'''
Created on 2016-10-3

@author: yimeng
'''
from rest_framework import serializers
from goods.models import Type,TypeAttr,Goods

class TypeSerializer(serializers.ModelSerializer):
    superiors_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Type
        fields = ('pk','name','superiors','superiors_name')
    
    def get_superiors_name(self,obj):
        if obj.superiors:
            return obj.superiors.name
        return None
    
    def validate_superiors(self, value):
        if value=='' or value is None:
            raise serializers.ValidationError("暂不支持多行业功能，请期待1.x版本的更新")
        else:
            return value
    
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
        
class GoodsSearchSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Goods
        fields = (
                  'pk',
                  'name',
                  'manufacturer',
                  'specification',
                  'unit',
                  'barcode',
                  'type',
                  'salesprice',
                  'static_attr'
                 )
    def get_type(self,obj):
        return obj.type.name