from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_pgjsonb import JSONField
import json

class TypeManager(models.Manager):
    def getsuperPk(self,tid):
        '''递归寻找对应商品类型的最顶层的祖先Pk'''
        supertype = Type.objects.get(pk=tid)
        if supertype.superiors is None or supertype.superiors.pk == 0:
            return supertype.pk
        else:
            superId = self.getsuperPk(supertype.superiors.pk)
        return superId

class Type(models.Model):
    name = models.CharField(max_length=30,unique=True)
    superiors = models.ForeignKey("self",blank=True,null=True,default=None)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    objects = TypeManager()

    def __str__(self):
        return self.name

class Goods(models.Model):
    gsav = JSONField()
    type = models.ForeignKey(Type)
    creator = models.ForeignKey(User,blank=True,null=True)
    lastmodifyer = models.ForeignKey(User,blank=True,null=True,related_name='lastmodifyer')
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return str(self.gsav.get('name','无名称'))
    def save(self,*args,**kwargs):
        self.gsav = json.loads(self.gsav)
        super(Goods,self).save(*args,**kwargs)
     

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