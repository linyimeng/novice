from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Department(models.Model):
    '''
    部门表
    '''
    name = models.CharField(_('department name'),max_length=60)
    superiors = models.ForeignKey('self',default=None,blank=True,null=True)
    customid = models.CharField(max_length=30,unique=True,null=True,default=None,blank=True)
    manager = models.ForeignKey('EmpInfo',related_name='empinfo',blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    class Meta:
        verbose_name = _('department')
    def __str__(self):
        return self.name
    
class Jobs(models.Model):
    '''
    职位表
    '''
    name = models.CharField(_('jobname'),max_length=30)
    department = models.ForeignKey(Department)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    class Meta:
        verbose_name = _('jobs')
    def __str__(self):
        return self.name
class EmpInfo(models.Model):
    '''
    员工信息
    '''
    user = models.OneToOneField(User)
    name = models.CharField(_('full name'),max_length=60)
    customid = models.CharField(max_length=30,blank=True,null=True,unique=True)
    department = models.ForeignKey(Department)
    job = models.ForeignKey(Jobs,blank=True,null=True)
    work_address = models.CharField(_('work address'),max_length=255,blank=True,null=True)
    office_phone = models.CharField(_('office phone'),max_length=12,unique=True,blank=True,null=True)
    office_address = models.CharField(_('office address'),max_length=255,blank=True,null=True)
    email = models.EmailField(unique=True)
    office_landline = models.CharField(_('landline'),max_length=20,blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    cardid = models.CharField(_('cardid'),max_length=20,blank=20,null=True)
    bank_account = models.CharField(_('bank Account'),max_length=36,blank=True,null=True)
    
    sex = models.CharField(_('sex'),max_length=2,blank=True,null=True)
    marital_status = models.CharField(_('marital status'),max_length=6,blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    
    isarchive = models.BooleanField(_('is archive'),default=False)
    entry_time = models.DateTimeField(blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    class Meta:
        verbose_name = _('staffinfo')
    def __str__(self):
        return self.name
    