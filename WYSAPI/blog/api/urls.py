from django.conf.urls import url
from blog.api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^article/$',views.ArticleListAPIView.as_view(),name="article-list"),
    url(r'^article/(?P<pk>[0-9]+)/$',views.ArticleRetrieveAPIView.as_view(),name='article-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)