'''
Created on 2017-1-14

@author: yimeng
'''
from django.conf.urls import url
from directsales import views
from directsales import ajaxchk
from directsales import ajax
from django.views.generic import TemplateView

urlpatterns = [
    url('^$',views.view_home),
    
    url('^login/$',views.login,name='login'),
    url('^logout/$',views.logout,name='logout'),
    url('^changepassword/$',views.changepassword,name="changepassword"),
    url('^changepaypassword/$',views.changepaypassword,name='changepaypassword'),
    
    url('^home/$',views.view_home,name="view-home"),
    
    url('^registered/$',views.registered,name="registered"),
    url('^registered/(?P<parentusername>[^/.]+)/(?P<isright>[^/.]+)/$',views.registered,name="registered_parent"),
    url('^upgrademember/$',views.upgrade_member,name="upgrade_member"),
    url('^memberlist/$',views.view_member_list,name="member-list"),
    url('^membertree/(?P<username>[^/.]+)/$',views.view_member_tree,name="view_member_tree_other"),
    url('^membertree/$',views.view_member_tree,name="view_member_tree"),
    url('^userinfo/$',views.doubletrackInfo,name="user-info"),
    url('^goods/$',views.view_goods,name="view_goods"),
    url('^createorder/$',views.createorder,name="createorder"),
    url('^orderhistory/$',views.orderhistory,name="orderhistory"),
    url('^createordersuccess/(?P<ordercode>[^/.]+)/$',views.createorder_success),
    url('^orderdetail/(?P<ordercode>[^/.]+)/$',views.orderdetail,name="orderdetail"),
    url('^address/$',views.add_address,name="add_address"),
    url('^shipgoods/$',views.shipgoods,name="shipgoods"),
    
    url('^bonusdetail/$',views.view_bonus_detail,name="view-bonus_detail"),
    url('^transfergold/$',views.transfer,name="transfergold"),
    url('^withdrawal/$',views.gold_withdrawal,name='withdrawal'),
    url('^withdrawalhistory',views.view_withdrawal_history,name="view-withdrawal-history"),
    url('^glodrecharge/$',TemplateView.as_view(template_name="directsales/success/glod_recharge.html"),name="glodrecharge"),
    
    url('^chkuser/$',ajaxchk.chkUser,name="chk-user"),
    url('^chkparent/$',ajaxchk.chkparenttrack,name="chk-parent"),
    url('^chktrack/$',ajaxchk.chkdoubletrack,name="chk-track"),
    url('^chkisright/$',ajaxchk.chkisright,name="chk-isright"),
    url('^chkisenough/$',ajaxchk.chkisenough,name="chk-isenough"),
    url('^chkverifycode/$',ajaxchk.chkverifycode,name="chk-chkverifycode"),
    url('^confirmpay/$',ajaxchk.confirmpay,name="confirmpay"),
    url('^chkpwd/$',ajaxchk.chkpwd,name="chkpwd"),
    url('^chkpaypwd/$',ajaxchk.chkpaypwd,name="chkpaypwd"),
    url('^verifycode/$',views.verifycode,name="chk-verifycode"),
    
    url('^success/(?P<template_path>[^/.]+)/$',views.success,name="success"),
    url('^goldwithdrawal/success/(?P<wh_pk>[^/.]+)$',views.gold_withdrawal_success),
    
    url('^getawardsstatisticsdata/$',ajax.get_awards_statistics_data,name="awards_statistics_data"),
    url('^ship/$',ajax.ship,name="ship"),
    url('^sendmail/$',views.send_email,name="send_mail"),
    
    url('^bulletinboard/$',views.bulletin_board,name="bulletinboard"),
    url('^confirmorder/$',ajax.confirmship,name="confirmship"),
    
]