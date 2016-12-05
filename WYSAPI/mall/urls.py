'''
Created on 2016-11-30

@author: yimeng
'''
from django.conf.urls import url
from mall import views
urlpatterns = [
    url('^$',views.view_home),
    url('^home/$',views.view_home,name="view-home"),
    
    url('^category/$',views.view_category_list,name='view-category'),
    
    url('^detail/$',views.view_detail,name='view-goods-detail'),
    
    url('^carts/$',views.view_carts,name="view-carts"),
    url('^confirmorder/$',views.view_confirm_order,name="view-confirm-order"),
    
    url('^my/$',views.view_user_center,name="view-user-center"),
    url('^myaddress/$',views.view_address,name="view-address"),
    url('^addaddress/$',views.add_address,name="add-address"),
    url('^myorder/$',views.view_order,name="view-order"),
    url('^mycollection/$',views.view_mycollection,name="view-collection"),
]