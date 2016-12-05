'''
Created on 2016-12-5

@author: yimeng
'''
from django.conf.urls import url
from file.views import ImageCreateAPIView
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns([
    url('^image/$',ImageCreateAPIView.as_view(),name='imgupload'),                                   
])
