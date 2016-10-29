'''
Created on 2016-10-5

@author: yimeng
'''
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from purchases.models import Purchase
from goods.models import Goods
from staff.models import EmpInfo

class PurchaseSerializer(ModelSerializer):
    goods_name = SerializerMethodField(write_only=True)
    creator_name = SerializerMethodField(write_only=True)
    class Meta:
        model = Purchase
        fields = (
                  'ordercode',
                  'quantity',
                  'purchaseprice',
                  'dynamic_attr',
                  'remark',
                  'goods',
                  'creator',
                  
                  'goods_name',
                  'creator_name',
                  )
        
    def get_goods_name(self,obj):
        return Goods.objects.get(pk=obj.goods).name;
    
    def get_creator_name(self,obj):
        return EmpInfo.objects.get(user__pk=obj.creator).name;