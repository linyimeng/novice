from django.conf.urls import include, url
from django.contrib import admin

api_urls = [
    url(r'^$',include('doc.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^employee/',include('employee.urls')),
    url(r'^goods/',include('goods.urls')),
    url(r'^partner/',include('partner.urls')),
    url(r'^order/',include('order.urls')),
    url(r'^fileupload/',include('file.urls')),
#     url(r'^mall/',include('mall.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
handler404 = 'directsales.views.page_not_found'
handler500 = 'directsales.views.page_error'
urlpatterns = [
    #不能使用namespace='first'
    url(r'^admin/',include(admin.site.urls)),
    url(r'^api/',include(api_urls)),
    url(r'^mall/',include('mall.urls',namespace="mall")),
    url(r'^directsale/',include('directsales.urls',namespace="directsale")),
]
