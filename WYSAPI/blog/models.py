from django.db import models
from django.contrib.auth.models import User
from plugin.editors.DjangoUeditor.models import UEditorField
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class BlogUser(models.Model):
    '''
    blog user
    '''
    user        = models.OneToOneField(User)
    nickname    = models.CharField(max_length=30,blank=True,unique=True,null=True)
    blogname    = models.CharField(max_length=30,unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    def __str__(self):
        return self.blogname

class Article(models.Model):
    '''
    article table
    '''
    title       = models.CharField(max_length=60)
    author      = models.ForeignKey(BlogUser)
    description = models.CharField(max_length=120)
    #content     = models.TextField(default='',blank=True)
    content = UEditorField('内容', height=300, width=1000,default='', blank=True, imagePath="uploads/images/",toolbars='besttome', filePath='uploads/files/')
    published   = models.BooleanField(default=True)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    comment table
    '''
    user        = models.CharField(max_length=30)
    article     = models.ForeignKey(Article)
    content     = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(_('deleted'),blank=True,null=True)
    
    def __str__(self):
        return self.content
    
