from django.db import models
from goods.models import Goods
from partner.models import Company,Personal
from django.utils.translation import ugettext_lazy as _
from django_pgjsonb import JSONField
from django.conf import settings
from django.contrib.auth.models import User
import json

DEFAULT_ORDER_STATUS = (
    ('N','Not reviewed'),
    ('R','Reviewed'),
    ('P','pay'),
    ('W','wait ship'),
    ('T','In transit'),
    ('D','Delivered'),
    ('I','Invoiced'),
    ('R','Return goods'),
    ('O','end')
)

class OrderManager(models.Manager):
    def get_order_status(self,order,code=False):
        
        assert isinstance(order, Order), (
            'order is not Order Object'
        )
        
        if code is False:
            status = self.__get_status_tuple(order.status[-1])
        else:
            status = order.status[-1]
        return status
        
    def __get_status_tuple(self,status):
        for s in Order.ORDER_STATUS:
            if status in s:
                return s[1]
        else:
            return 'No status'

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
    ORDER_STATUS = settings.MALL.get('ORDER_STATUS',DEFAULT_ORDER_STATUS)
    ordercode = models.CharField(max_length=30,primary_key=True)
    company = models.ForeignKey(Company,blank=True,null=True)
    personal= models.ForeignKey(User,blank=True,null=True,related_name='personal')
    type = models.ForeignKey(Type)
    status = models.CharField(max_length=10,choices=ORDER_STATUS,default='N')
    
    totalquantity = models.DecimalField(max_digits=10,decimal_places=2)
    totalprice = models.DecimalField(max_digits=18,decimal_places=8)
    
    recipient = models.CharField(max_length=30,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    address = models.CharField(max_length=300,blank=True,null=True)
    
    remark = models.TextField(blank=True,null=True)
    creator = models.ForeignKey(User)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    objects = OrderManager()
    
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
        return self.goods.gsav['name']
    
    def save(self,*args,**kwargs):
        self.gsav = json.loads(self.gsav)
        self.gdav = json.loads(self.gdav)
        super(Detail,self).save(*args,**kwargs)
    
    
    