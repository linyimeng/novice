from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
class UserInfo(models.Model):
    '''
    这是一个总的用户表，所有用户表都需要与此关联
    '''
    user = models.OneToOneField(User)
    name = models.CharField(_('nickname'),max_length=60)
    phone = models.CharField(max_length=11,unique=True,blank=True,null=True)
    qq = models.CharField(max_length=13,unique=True,blank=True,null=True)
    wx = models.CharField(max_length=20,unique=True,blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('WYSuser')
        verbose_name_plural = _('WYSusers')
    