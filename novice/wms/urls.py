'''
Created on 2016-11-9

@author: yimeng
'''
from django.conf.urls import url
from wms import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^goods/$',views.GoodsListAPIView.as_view(),name='wmsgoods-list'),
])