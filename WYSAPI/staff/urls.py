'''
Created on 2016-9-20

@author: yimeng
'''
from django.conf.urls import url,include
from staff import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'jobs',views.JobsViewSet)
router.register(r'emp',views.EmpInfoViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]