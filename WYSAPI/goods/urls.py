'''
Created on 2016-10-3

@author: yimeng
'''
from django.conf.urls import url
from goods import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^goods/$',views.GoodsListCreateAPIView.as_view(),name='goods-list'),
    url(r'^goods/(?P<pk>[^/.]+)/$',views.GoodsRetrieveUpdateDestroyAPIView.as_view(),name='goods-detail'),
    url(r'^attrs/$',views.TypeAttrCreateAPIView.as_view(),name='typeattr-create'),
    url(r'^attrs/(?P<gtid>[0-9]+)/$',views.TypeAttrListAPIView.as_view(),name='goodsattr-all-list'),
    url(r'^attrs/(?P<gtid>[0-9]+)/(?P<type>[a-z]+)/$',views.TypeAttrListAPIView.as_view(),name='goodsattr-list'),
    url(r'^attr/(?P<keyname>[^/.]+)/$',views.TypeAttrRetrieveUpdateDestroyAPIView.as_view(),name='goodsattr-detail'),
])