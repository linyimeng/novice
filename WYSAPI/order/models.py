from django.db import models
from staff.models import EmpInfo
from goods.models import Goods
from BP.models import Company,Personal
from django.utils.translation import ugettext_lazy as _
from django_pgjsonb import JSONField
import json
class Type(models.Model):
    IN = 'I'
    OUT= 'O'
    IN_OR_OUT = (
        (IN,'in'),
        (OUT,'out'),
    )
    name = models.CharField(max_length=30)
    io =  models.CharField(max_length=1,choices=IN_OR_OUT)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    ordercode = models.CharField(max_length=30,primary_key=True)
    company = models.ForeignKey(Company,blank=True,null=True)
    personal= models.ForeignKey(Personal,blank=True,null=True)
    type = models.ForeignKey(Type)
    
    totalquantity = models.DecimalField(max_digits=10,decimal_places=2)
    totalprice = models.DecimalField(max_digits=18,decimal_places=8)
    
    remark = models.TextField(blank=True,null=True)
    creator = models.ForeignKey(EmpInfo)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.ordercode

class Detail(models.Model):
    order = models.ForeignKey(Order)
    goods = models.ForeignKey(Goods)
    
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=18,decimal_places=8)
    
    gdav = JSONField()
    gsav = JSONField()
    
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.goods.name
    
    def save(self,*args,**kwargs):
        self.gsav = json.loads(self.gsav)
        self.gdav = json.loads(self.gdav)
        super(Detail,self).save(*args,**kwargs)
    
    
    