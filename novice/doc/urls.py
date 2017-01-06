'''
Created on 2016-12-31

@author: yimeng
'''
from django.conf.urls import url
from doc import views

urlpatterns = [
    url(r'^$',views.api_root),
]