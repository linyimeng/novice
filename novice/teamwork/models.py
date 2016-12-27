from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class twModel(models.Model):
    '''定义通用字段类'''
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User)
    manager = models.ForeignKey(User)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
class Projects(twModel):
    '''项目'''
    name = models.CharField(max_length=30)

class Modules(twModel):
    '''模块'''
    project = models.ForeignKey(Projects)
    name = models.CharField(max_length=30)
    superiors = models.ForeignKey("self",blank=True,null=True,default=None)
    
class Components(twModel):
    '''组件'''
    module = models.ForeignKey(Modules)
    name = models.CharField(max_length=30)
    
class Flows(models.Model):
    '''定义完成步骤'''
    name = models.CharField(max_length=30)
    
class Bugs(twModel):
    '''问题'''
    component = models.ManyToManyField(Components)
    name = models.CharField(max_length=30)
    
class Solutions(twModel):
    '''解决之道'''
    bug = models.ForeignKey(Bugs)
    name = models.CharField(max_length=30)

    
    