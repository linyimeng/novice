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
    #处理customid为‘’的情况
    def validate_customid(self,value):
        if value == '':
            value = None
        return value
    def validate_sav(self,value):
        try:
            sav = loads(value)
        except ValueError:
            raise serializers.ValidationError("不是合法的json数据")
        keys = sav.keys()
        attrs = TypeAttr.objects.filter(type='ss')
        self.checkkey(attrs, keys)
        return value
    def checkkey(self,attrs,keys):
        for attr in attrs:
            if attr.keyname not in keys:
                raise serializers.ValidationError("数据非法，系统定义属性不能为空,当前系统自定义可调用相关接口查看，具体调用方法查看接口文档")