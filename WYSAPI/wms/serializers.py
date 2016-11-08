'''
Created on 2016-11-8

@author: yimeng
'''
from order.models import Detail
from rest_framework import serializers
from django.db.models import Sum

class GoodsListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    manufacturer = serializers.SerializerMethodField()
    specification = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    barcode = serializers.SerializerMethodField()
    salesprice = serializers.SerializerMethodField()
    static_attr = serializers.SerializerMethodField()
    inventory = serializers.SerializerMethodField()
    class Meta:
        model = Detail
        fields = (
                  'price',
                  'validity',
                  'productiondate',
                  'batch',
                  'dynamic_attr',
                  'goods',
                  'name',
                  'manufacturer',
                  'specification',
                  'unit',
                  'barcode',
                  'salesprice',
                  'static_attr',
                  'inventory'
                 )
    def get_name(self,obj):
        return obj.goods.name;
    def get_manufacturer(self,obj):
        return obj.goods.manufacturer
    def get_specification(self,obj):
        return obj.goods.specification
    def get_unit(self,obj):
        return obj.goods.unit
    def get_barcode(self,obj):
        return obj.goods.barcode
    def get_salesprice(self,obj):
        return obj.goods.salesprice
    def get_static_attr(self,obj):
        return obj.goods.static_attr
    def get_inventory(self,obj):
        inquantity = Detail.objects.filter(order__type__io='I',goods=obj.goods).aggregate(inventory = Sum('quantity')).get('inventory') or 0
        outquantity = Detail.objects.filter(order__type__io='O',goods=obj.goods).aggregate(inventory = Sum('quantity')).get('inventory') or 0
        inventory = inquantity - outquantity
        return inventory;