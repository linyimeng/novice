from django.db import models
from user.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class WeChatUser(models.Model):
    user = models.OneToOneField(User)
    wxopenid = models.CharField(max_length=60, blank=True,null=True)
    wxuserid = models.CharField(max_length=60, blank=True,null=True)
    wxnickname = models.CharField(max_length=60,blank=True,null=True)
    wxsex = models.CharField(max_length=1,blank=True,null=True)
    wxcity = models.CharField(max_length=60,blank=True,null=True)
    wxprovince = models.CharField(max_length=60,blank=True,null=True)
    wxlanguage = models.CharField(max_length=30,blank=True,null=True)
    wxheadimgurl = models.CharField(max_length=365,blank=True,null=True)
    wxsubscribe_time = models.CharField(max_length=10,blank=True,null=True)
    wxunionid = models.CharField(max_length=30,blank=True,null=True)
    wxremark = models.TextField(blank=True,null=True)
    wxgroupid = models.CharField(max_length=20,blank=True,null=True)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    class Meta:
        verbose_name = _('wechatuser')