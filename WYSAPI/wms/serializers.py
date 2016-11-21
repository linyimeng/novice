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
    class Meta:
        model = Detail
        fields = (
                  'gpk',
                  'gsav',
                  'gdav',
                 )
    def get_gpk(self,obj):
        return obj.goods.pk
        
    def get_gsav(self,obj):
        return obj.gsav
    def get_gdav(self,obj):
        return obj.gdav
    