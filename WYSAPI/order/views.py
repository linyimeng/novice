'''
Created on 2016-10-29

@author: yimeng
'''
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from django.db import transaction

class OrderCreateAPIView(CreateAPIView):
    pass