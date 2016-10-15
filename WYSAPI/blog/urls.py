from django.conf.urls import url
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns
'''
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'article',views.ArticleViewSet)
router.register(r'user',views.BlogUserViewSet)
router.register(r'comment',views.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
'''
urlpatterns = [
    #url(r'^$',views.api_root),
    url(r'^articles/$',views.article_list),
    url(r'^article/(?P<pk>[0-9]+)/$',views.article_detail),
    url(r'user/(?P<pk>[0-9]+)/$',views.BlogUserDetailAPIView.as_view()),
    url(r'comments/(?P<apk>[0-9]+)/$',views.CommentList.as_view(),name='comment-list'),
    url(r'comment/(?P<pk>[0-9]+)/$',views.CommentDetail.as_view(),name='comment-detail'),
    url(r'atest/$',views.atest),
]

urlpatterns = format_suffix_patterns(urlpatterns)