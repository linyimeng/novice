'''
Created on 2016-10-29

@author: yimeng
'''
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from purchases.serializers import PurchaseSerializer
from purchases.models import Purchase

class PurchaseListCreateAPIView(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer