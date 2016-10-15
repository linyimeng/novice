'''
Created on 2016-10-5

@author: yimeng
'''
from django.conf.urls import url,include
from BP.views import PersonalViewSet
from purchases import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'company', views.VendorsViewSet)
router.register(r'personal',PersonalViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]