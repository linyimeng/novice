'''
Created on 2016-11-3

@author: yimeng
'''
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from order.models import Type,Order,Detail
class TypeSerializer(ModelSerializer):
    '''
    订单类型
    '''
    class Meta:
        model = Type
        fields = ('name','io')
        
class DetailSerializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = ('order','goods','gdav','gsav','quantity','price')
        
        
class DetailRetrieveSerializer(ModelSerializer):
    gdav = SerializerMethodField()
    gsav = SerializerMethodField()
    class Meta:
        model = Detail
        fields = ('order','goods','gdav','gsav','quantity','price')
    def get_gdav(self,obj):
        gdav = obj.gdav
        return gdav
    def get_gsav(self,obj):
        gsav = obj.gsav
        return gsav

#报表相关
class OrderGoodsInOrOutSerializer(DetailRetrieveSerializer):
    '''入出库明细'''
    companyname = SerializerMethodField()
    company = SerializerMethodField()
    class Meta:
        model = Detail
        fields = ('order','goods','gdav','gsav','quantity','price','joined','companyname','company')
    def get_companyname(self,obj):
        company_name = obj.order.company.name
        return company_name
    def get_company(self,obj):
        return obj.order.company.pk
        
        
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
                  'ordercode',
                  'totalquantity',
                  'totalprice',
                  'company',
                  'type',
                  'remark',
                  'creator',
                 )

class OrderListSerializer(ModelSerializer):
    company = SerializerMethodField()
    type = SerializerMethodField()
    creator = SerializerMethodField()
    class Meta:
        model = Order
        fields = (
                  'ordercode',
                  'totalquantity',
                  'totalprice',
                  'joined',
                  'company',
                  'type',
                  'remark',
                  'creator'
                 )
    def get_company(self,obj):
        if obj.company:
            return obj.company.name
        return None
    
    def get_type(self,obj):
        return obj.type.name
    
    def get_creator(self,obj):
        return obj.creator.name

class OrderRetrieveSerializer(ModelSerializer):
    company = SerializerMethodField()
    type = SerializerMethodField()
    creator = SerializerMethodField()
    detail = SerializerMethodField()
    class Meta:
        model = Order
        fields = (
                  'ordercode',
                  'totalquantity',
                  'totalprice',
                  'joined',
                  'company',
                  'type',
                  'remark',
                  'creator',
                  'detail'
                 )
    def get_company(self,obj):
        return obj.company.name
    
    def get_type(self,obj):
        return obj.type.name
    
    def get_creator(self,obj):
        return obj.creator.name

    def get_detail(self,obj):
        detail_set = Detail.objects.filter(order__pk=obj.ordercode)
        detail = DetailRetrieveSerializer(detail_set,many=True).data
        return detail
        
        
        
        
        
        
        
        