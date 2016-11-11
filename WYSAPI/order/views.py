'''
Created on 2016-10-29

@author: yimeng
'''
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from order.serializers import OrderSerializer,DetailSerializer,TypeSerializer,OrderListSerializer,OrderRetrieveSerializer
from order.models import Type,Order,Detail
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

class TypeListAPIView(ListAPIView):
    '''
    订单类型查询，默认提供两种类型，进货单和销售单
    '''
    serializer_class = TypeSerializer
    def get_queryset(self,*args,**kwargs):
        io = self.kwargs['io']
        io = str.upper(io)
        queryset_list = Type.objects.filter(io=io)
        return queryset_list
    
class OrderGoodsInOrOutListAPIView(ListAPIView):
    serializer_class = DetailSerializer
    def get_queryset(self,*args,**kwargs):
        io = self.kwargs['io']
        io = str.upper(io)
        queryset_list = Detail.objects.filter(order__type__io=io).order_by('order')
        return queryset_list
class OrderCreateAPIView(APIView):
    '''
    {
        "order": {
            "ordercode": "",
            "company": null,
            "type": null,
            "remark": "",
            "creator": null
        },
        "detail": [{
            "order": "",
            "productiondate":"",
            "validity":"",
            "batch":"",
            "goods"null:,
            "quantity": null,
            "price": null,
            "dynamic_attr": "",
            "remark": ""
        }]
    }
    '''
    def post(self, request,format=None):
        main = self.sum(request)
        detail = request.data.get('detail')
        with transaction.atomic():
            order_serializer = OrderSerializer(data=main,context={'request':request})
            #raise_exception=True出现异常引发数据库回滚
            if order_serializer.is_valid(raise_exception=True):
                order_serializer.save()
                print(order_serializer.data)
                #ordercode = order_serializer.data.get('ordercode')
            else:
                return Response(order_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            detail_serializer = DetailSerializer(data=detail,many=True)
            if detail_serializer.is_valid(raise_exception=True):
                detail_serializer.save()
                return Response(order_serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(detail_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def sum(self,request):
        '''
        计算总价和总数
        '''
        main = request.data.get('order')
        detail = request.data.get('detail')
        total_quantity = 0
        total_price = 0
        for od in detail:
            total_price = total_price + (od.get('price') * od.get('quantity'))
            total_quantity = total_quantity + od.get('quantity')
        main['totalquantity'] = total_quantity
        main['totalprice'] = total_price
        return main
    
class OrderIOListAPIView(ListAPIView):
    serializer_class = OrderListSerializer
    def get_queryset(self,*args,**kwargs):
        io = self.kwargs['io']
        io = str.upper(io)
        queryset_list = Order.objects.filter(type__io=io)
        return queryset_list
    
class OrderDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer
    lookup_field = 'ordercode'
        
        
        

