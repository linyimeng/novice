'''
Created on 2016-10-5

@author: yimeng
'''
from django.conf.urls import url,include
from BP import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'personal',views.PersonalViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]