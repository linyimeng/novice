'''
Created on 2016-11-10

@author: yimeng
'''
from django.conf.urls import url
from blog import views

urlpatterns = [
    url('^$',views.article_list),
    url('^article/$',views.article_list,name='article-list'),
    url('^article/(?P<pk>[0-9]+)/$',views.article_detail,name='article-detail'),
    url('^comment/create/(?P<apk>[0-9]+)/$',views.comment_create,name='comment-create'),
]