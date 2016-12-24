from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Images(models.Model):
    img = models.ImageField(upload_to="images")
    type = models.CharField(max_length=20)
    
    creator = models.ForeignKey(User)
    joined = models.DateTimeField(_('joined'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)
    
    def __str__(self):
        return self.img