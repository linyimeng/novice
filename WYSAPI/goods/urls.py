'''
Created on 2016-10-3

@author: yimeng
'''
from django.conf.urls import url,include
from goods import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'type', views.TypeViewSet)
router.register(r'attr',views.TypeAttrViewSet)
router.register(r'goods',views.GoodsViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]