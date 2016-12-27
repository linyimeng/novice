from django.conf.urls import url
from user.views import UserLoginAPIView, UserLogoutAPIView,UserCreateAPIView
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^$',UserCreateAPIView.as_view(),name="create"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name="logout"),
]

urlpatterns = format_suffix_patterns(urlpatterns)