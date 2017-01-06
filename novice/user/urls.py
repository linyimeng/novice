from django.conf.urls import url
from user.views import UserLoginAPIView, UserLogoutAPIView,UserCreateAPIView,api_root
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^$',UserCreateAPIView.as_view(),name="create"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name="logout"),
    url(r'^doc/$',api_root,name="user-doc"),
]

urlpatterns = format_suffix_patterns(urlpatterns)