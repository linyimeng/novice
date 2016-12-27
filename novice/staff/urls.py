'''
Created on 2016-9-20
@author: yimeng
'''
from django.conf.urls import url,include
from staff import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'jobs',views.JobsViewSet)
router_urls = [
    url(r'^',include(router.urls)),
]

jobs_urls = format_suffix_patterns([
    url(r'^djobs/(?P<dpk>[^/.]+)/$',views.JobsListAPIView.as_view(),name='djobs-list')           
])

emp_urls = format_suffix_patterns([
    url(r'^emps/$',views.EmpInfoListAPIView.as_view(),name='emps-list'),
    url(r'^emp/$',views.EmpInfoCreateAPIView.as_view(),name='emps-create'),
    url(r'^emp/(?P<pk>[^/.]+)/$',views.EmpInfoRetrieveUpdateAPIView.as_view(),name='emps-detail'),
    url(r'^emp/user/(?P<user>[^/.]+)/$',views.EmpInfoRetrieveAPIView.as_view(),name='emps-user-detail'),
])

urlpatterns = emp_urls + router_urls + jobs_urls