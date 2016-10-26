from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Type(models.Model):
    name = models.CharField(max_length=30)
    superiors = models.ForeignKey("self",blank=True,null=True,default=None)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name

class Goods(models.Model):
    customid = models.CharField(max_length=30,unique=True,blank=True,null=True)
    name = models.CharField(max_length=120)
    manufacturer = models.CharField(max_length=226)
    barcode = models.CharField(max_length=30,blank=True,null=True)
    salesprice = models.DecimalField(max_digits=12,decimal_places=4)
    costprice = models.DecimalField(max_digits=12,decimal_places=4)
    type = models.ForeignKey(Type)
    is_active = models.BooleanField(default=True)
    main_attr = models.TextField(blank=True,null=True)
    custom_attr = models.TextField(blank=True,null=True)
    other_attr = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User)
    lastmodifyer = models.ForeignKey(User,blank=True,null=True,related_name='lastmodifyer')
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name
    

class TypeAttr(models.Model):
    MAIN_ATTR_TYPE = 'main'
    OTHER_ATTR_TYPE= 'other'
    CUSTOM_ATTR_TYPE='custom'
    ATTR_TYPE_CHOICES = (
        (MAIN_ATTR_TYPE,'main_attr'),
        (OTHER_ATTR_TYPE,'other_attr'),
        (CUSTOM_ATTR_TYPE,'custom_attr'),
    )
    goodstype = models.ForeignKey(Type)
    name = models.CharField(max_length=30)
    attr_type = models.CharField(max_length=6,choices=ATTR_TYPE_CHOICES,default=MAIN_ATTR_TYPE)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
    
    
    