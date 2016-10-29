from django.db import models
from staff.models import EmpInfo
from goods.models import Goods
# Create your models here.

class Purchase(models.Model):
    ordercode = models.CharField(max_length=30,primary_key=True)
    goods = models.ForeignKey(Goods)
    
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    purchaseprice = models.DecimalField(max_digits=10,decimal_places=10)
    
    dynamic_attr = models.TextField(blank=True,null=True)
    
    remark = models.TextField(blank=True,null=True)
    creator = models.ForeignKey(EmpInfo)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    