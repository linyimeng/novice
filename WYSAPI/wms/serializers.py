'''
Created on 2016-11-8
@author: yimeng
'''
from order.models import Detail
from rest_framework import serializers
from django.db.models import Sum

class GoodsListSerializer(serializers.ModelSerializer):
    gsav = serializers.SerializerMethodField()
    gdav = serializers.SerializerMethodField()
    gpk = serializers.SerializerMethodField()
    inventory = serializers.SerializerMethodField()
    class Meta:
        model = Detail
        fields = (
                  'gpk',
                  'gsav',
                  'gdav',
                  'inventory',
                 )
    def get_gpk(self,obj):
        return obj.goods.pk
        
    def get_gsav(self,obj):
        return obj.gsav
    def get_gdav(self,obj):
        return obj.gdav
    def get_inventory(self,obj):
        in_inventory = Detail.objects.filter(goods=obj.goods,order__type__io='I').aggregate(in_inventory=Sum('quantity')).get('in_inventory',0)
        out_inventory= Detail.objects.filter(goods=obj.goods,order__type__io='O').aggregate(out_inventory=Sum('quantity')).get('out_inventory',0)
        if in_inventory is None:
            in_inventory = 0
        if out_inventory is None:
            out_inventory = 0
        inventory = in_inventory - out_inventory
        return inventory