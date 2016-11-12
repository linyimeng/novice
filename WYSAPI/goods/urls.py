'''
Created on 2016-10-3

@author: yimeng
'''
from django.conf.urls import url,include
from goods import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'type', views.TypeViewSet)
router.register(r'goods',views.GoodsViewSet)
router_urls = [
    url(r'^',include(router.urls)),
]

typearre_urls = format_suffix_patterns([
    url(r'^attrs/$',views.TypeAttrCreateAPIView.as_view(),name='typeattr-create'),
    url(r'^attrs/(?P<gtid>[0-9]+)/$',views.TypeAttrListAPIView.as_view(),name='goodsattr-all-list'),
    url(r'^attrs/(?P<gtid>[0-9]+)/(?P<type>[a-z]+)/$',views.TypeAttrListAPIView.as_view(),name='goodsattr-list'),
    url(r'^attr/(?P<keyname>[^/.]+)/$',views.TypeAttrRetrieveUpdateDestroyAPIView.as_view(),name='goodsattr-detail'),
    
])

urlpatterns = typearre_urls + router_urls