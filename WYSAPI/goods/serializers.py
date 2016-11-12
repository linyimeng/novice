'''
Created on 2016-10-3

@author: yimeng
'''
from rest_framework import serializers
from goods.models import Type,TypeAttr,Goods
from json import loads
class TypeSerializer(serializers.ModelSerializer):
    '''
    商品类别，现只支持单一行业商品
    '''
    superiors_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Type
        fields = ('pk','name','superiors','superiors_name')
    
    def get_superiors_name(self,obj):
        if obj.superiors:
            return obj.superiors.name
        return None
    
    def validate_superiors(self, value):
        '''
        检查处理superiors为空或者有父类别的情况
        '''
        if value=='' or value is None:
            raise serializers.ValidationError("暂不支持多行业功能，请期待1.x版本的更新")
        else:
            return value
    
class TypeAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAttr
        fields= ('goodstype','keyname','name','type')
        
        
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields=(
                'pk',
                'customid',
                'type',
                'sav'
                )
    
    def validate_sav(self,value):
        try:
            loads(value)
        except ValueError:
            raise serializers.ValidationError("不是合法的json数据")
        return value