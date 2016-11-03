'''
Created on 2016-10-29

@author: yimeng
'''
from rest_framework.views import APIView
from order.serializers import OrderSerializer,DetailSerializer
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

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
        main = request.data.get('order')
        detail = request.data.get('detail')
        '''
        计算总价和总数
        '''
        total_quantity = 0
        total_price = 0
        for od in detail:
            total_price = total_price + od.get('price')
            total_quantity = total_quantity + od.get('quantity')
        main['totalquantity'] = total_quantity
        main['totalprice'] = total_price
        return main

