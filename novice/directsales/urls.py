'''
Created on 2017-1-14

@author: yimeng
'''
from django.conf.urls import url
from directsales import views
from directsales import ajaxchk
from directsales import ajax
urlpatterns = [
    url('^$',views.view_home),
    
    url('^login/$',views.login,name='login'),
    url('^logout/$',views.logout,name='logout'),
    url('^changepassword/$',views.changepassword,name="changepassword"),
    
    url('^home/$',views.view_home,name="view-home"),
    
    url('^registered/$',views.registered,name="registered"),
    url('^upgrademember/$',views.upgrade_member,name="upgrade_member"),
    url('^memberlist/$',views.view_member_list,name="member-list"),
    url('^membertree/$',views.view_member_tree,name="view_member_tree"),
    url('^userinfo/$',views.doubletrackInfo,name="user-info"),
    
    url('^bonusdetail/$',views.view_bonus_detail,name="view-bonus_detail"),
    url('^transfergold/$',views.transfer_gold,name="transfergold"),
    url('^withdrawal/$',views.gold_withdrawal,name='withdrawal'),
    url('withdrawalhistory',views.view_withdrawal_history,name="view-withdrawal-history"),
    
    
    url('^chkuser/$',ajaxchk.chkUser,name="chk-user"),
    url('^chkparent/$',ajaxchk.chkparenttrack,name="chk-parent"),
    url('^chktrack/$',ajaxchk.chkdoubletrack,name="chk-track"),
    url('^chkisright/$',ajaxchk.chkisright,name="chk-isright"),
    url('^chkisenough/$',ajaxchk.chkisenough,name="chk-isenough"),
    url('^chkverifycode/$',ajaxchk.chkverifycode,name="chk-chkverifycode"),
    url('^confirmpay/$',ajaxchk.confirmpay,name="confirmpay"),
    url('^chkpwd/$',ajaxchk.chkpwd,name="chkpwd"),
    url('^verifycode/$',views.verifycode,name="chk-verifycode"),
    
    url('^getawardsstatisticsdata/$',ajax.get_awards_statistics_data,name="awards_statistics_data"),
    
    url('^test/$',ajax.test),
]