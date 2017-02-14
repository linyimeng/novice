'''
Created on 2016-12-24

@author: yimeng
'''
from django.db import models
from django.contrib.auth.models import User
from goods.models import Goods
class Collection(models.Model):
    user = models.ForeignKey(User)
    goods= models.ForeignKey(Goods)
    
    joined = models.DateTimeField(auto_now_add=True)
    

class Shippingaddress(models.Model):
    user = models.ForeignKey(User)
    recipient = models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    province = models.CharField(max_length=20,blank=True,null=True)
    city = models.CharField(max_length=20,blank=True,null=True)
    county = models.CharField(max_length=20,blank=True,null=True)
    address = models.CharField(max_length=300)
    is_default = models.NullBooleanField(default=False,blank=True,null=True)
    
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)