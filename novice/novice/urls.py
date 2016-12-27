from django.conf.urls import include, url
from django.contrib import admin

api_urls = [
    url(r'^user/',include('user.urls')),
    url(r'^staff/',include('staff.urls')),
    url(r'^goods/',include('goods.urls')),
    url(r'^bp/',include('bp.urls')),
    url(r'^order/',include('order.urls')),
    url(r'^wms/',include('wms.urls')),
    url(r'^fileupload/',include('file.urls')),
#     url(r'^mall/',include('mall.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = [
    #不能使用namespace='first'
    url(r'^admin/',include(admin.site.urls)),
    url(r'^api/',include(api_urls)),
    url(r'^accounts/login/', 'blog.views.loginx'),
    url(r'^mall/',include('mall.urls',namespace="mall")),
]