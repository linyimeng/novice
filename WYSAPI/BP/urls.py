'''
Created on 2016-10-5

@author: yimeng
'''
from django.conf.urls import url,include
from BP import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'personal',views.PersonalViewSet)
router_urls = [
    url(r'^',include(router.urls)),
]

company_urls = format_suffix_patterns([
    url(r'^companytype/(?P<companytype>[^/.]+)/$',views.CompanyListAPIView.as_view(),name='company-list'),
    url(r'^company/(?P<pk>[^/.]+)/$',views.CompanyRetrieveUpdateDestroyAPIView.as_view(),name='company-detail'),
    url(r'^company/$',views.CompanyCreateAPIView.as_view(),name='company-create'),                                      
])

urlpatterns = company_urls + router_urls