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
    
