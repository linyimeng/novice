from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_pgjsonb import JSONField


class Type(models.Model):
    name = models.CharField(max_length=30,unique=True)
    superiors = models.ForeignKey("self",blank=True,null=True,default=None)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name

class Goods(models.Model):
    customid = models.CharField(max_length=30,unique=True,blank=True,null=True)
    sav = JSONField()
#     name = models.CharField(max_length=120)
#     manufacturer = models.CharField(max_length=226)
#     specification= models.CharField(max_length=30,blank=True,null=True)
#     unit = models.CharField(max_length=10,blank=True,null=True)
#     barcode = models.CharField(max_length=30,blank=True,null=True)
#     salesprice = models.DecimalField(max_digits=12,decimal_places=4)
#     costprice = models.DecimalField(max_digits=12,decimal_places=4)
    type = models.ForeignKey(Type)
#     is_active = models.BooleanField(default=True)
#     static_attr = models.TextField(blank=True,null=True)
#     #dynamic_attr = models.TextField(blank=True,null=True)
#     remark = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User,blank=True,null=True)
    lastmodifyer = models.ForeignKey(User,blank=True,null=True,related_name='lastmodifyer')
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    

class TypeAttr(models.Model):
    STATIC_ATTR_TYPE = 's'
    DYNAMIC_ATTR_TYPE= 'd'
    SYSTEM_STATIC_ATTR_TYPE = 'ss'
    SYSTEM_DYNAMIC_ATTR_TYPE = 'sd'
    ATTR_TYPE_CHOICES = (
        (STATIC_ATTR_TYPE,'static'),
        (DYNAMIC_ATTR_TYPE,'dynamic'),
        (SYSTEM_STATIC_ATTR_TYPE,'system_static'),
        (SYSTEM_DYNAMIC_ATTR_TYPE,'system_dynamic'),
    )
    goodstype = models.ForeignKey(Type)
    name = models.CharField(max_length=30,blank=True,null=True)
    keyname = models.CharField(max_length=30,unique=True)
    type = models.CharField(max_length=2,choices=ATTR_TYPE_CHOICES,default=STATIC_ATTR_TYPE)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    