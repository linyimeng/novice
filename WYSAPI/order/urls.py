'''
Created on 2016-10-5

@author: yimeng
'''
from django.conf.urls import url
from order import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    url(r'^type/(?P<io>[^/.]+)/$',views.TypeListAPIView.as_view(),name='type-list'),
    url(r'^list/io/(?P<io>[^/.]+)/$',views.OrderIOListAPIView.as_view(),name='order-list-io'),
    url(r'^create/$',views.OrderCreateAPIView.as_view(),name='order-create'),
    url(r'^(?P<ordercode>[^/.]+)/$',views.OrderDetailRetrieveAPIView.as_view(),name='order-detail'),
    url(r'^ordergoods/(?P<io>[^/.]+)/$',views.OrderGoodsInOrOutListAPIView.as_view(),name='order-goods-list'),
])