from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your models here.

class EmailhistoryManager(Manager):
    def send_mail_save(self, *args, **kwargs):
        to_mail = []
        to_mail.append(kwargs['to_email'])
        send_mail(kwargs['subject'], kwargs['message'], kwargs['from_email'],
                  to_mail, fail_silently=False)
        Emailhistory.objects.create(**kwargs)
#         Emailhistory.objects.create(user=kwargs['user'],subject=kwargs['subject'],message=kwargs['message'], 
#                                     from_email=kwargs['from_email'], to_email=kwargs['to_email'])

class Emailhistory(models.Model):
    user = models.ForeignKey(User)
    subject = models.CharField(max_length=120, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    from_email = models.EmailField()
    to_email = models.EmailField()
    joined = models.DateTimeField(auto_now_add=True)
    
    objects = EmailhistoryManager()
    