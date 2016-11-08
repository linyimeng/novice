from django.db import models
from staff.models import EmpInfo
from goods.models import Goods
from BP.models import Company
from django.utils.translation import ugettext_lazy as _

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
    
    validity = models.DateField(blank=True,null=True)
    productiondate = models.DateField(blank=True,null=True)
    batch = models.CharField(max_length=36,blank=True,null=True)
    
    dynamic_attr = models.TextField(blank=True,null=True)
    
    remark = models.TextField(blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.goods.name
    
    
    