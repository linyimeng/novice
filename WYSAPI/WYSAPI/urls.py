from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from plugin.editors.DjangoUeditor import urls as ueditorurl
api_urls = [
    url(r'^user/',include('user.urls')),
    url(r'^blog/',include('blog.api.urls')),
    url(r'^staff/',include('staff.urls')),
    url(r'^goods/',include('goods.urls')),
    url(r'^bp/',include('BP.urls')),
    url(r'^order/',include('order.urls')),
    url(r'^wms/',include('wms.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = [
    #不能使用namespace='first'
    url(r'^admin/',include(admin.site.urls)),
    url(r'^api/',include(api_urls)),
    url(r'^ueditor/', include(ueditorurl)),
    url(r'^blog/',include('blog.urls')),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)