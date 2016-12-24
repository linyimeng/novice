from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=80)
    customid = models.CharField(max_length=30,unique=True,blank=True,null=True)
    is_vendor = models.BooleanField(_('is vendor'),default=False)
    is_client = models.BooleanField(_('is client'),default=False)
    
    landline = models.CharField(_('landline'),max_length=20,blank=True,null=True)
    phone = models.CharField(_('phone'),max_length=12,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    fax = models.CharField(_('fax'),max_length=30,blank=True,null=True)
    address = models.CharField(max_length=225,blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    imgurl = models.CharField(max_length=120,blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Personal(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,blank=True,null=True)
    company = models.ForeignKey(Company,blank=True,null=True)
    job = models.CharField(max_length=20,blank=True,null=True)
    is_job = models.BooleanField(default=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    
    landline = models.CharField(_('landline'),max_length=20,blank=True,null=True)
    phone = models.CharField(_('phone'),max_length=12,unique=True,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    fax = models.CharField(_('fax'),max_length=30,blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    imgurl = models.CharField(max_length=120,blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name