from django.contrib import admin
from directsales.models import Doubletrack,Memberlevel,Bonus,Transactionhistory,Awards,Withdrawhistory,Goods,Order,Orderdetail
from django.core.exceptions import ObjectDoesNotExist
# Register your models here.
class DoubletrackAdmin(admin.ModelAdmin):
    '''节点'''
    #列表显示
    list_display = ('user','name','identity','parent','isright','directpushuser','phone','joined','updated')
    #搜索
    search_fields=('user__username','name','phone')
    #过滤器
    list_filter = ('identity',)
    #日期字段进行层次划分
    date_hierarchy = 'joined'
    
class MemberlevelAdmin(admin.ModelAdmin):
    '''会员等级'''
    list_display = ('__str__','price','joined')

class BonusAdmin(admin.ModelAdmin):
    '''用户金额账户'''
    list_display = ('username','name','identity','gold','freeze_gold','integral','shoppingcoupons','updater','updated')
    search_fields = ('track__user__username','track__name')
    list_filter = ('track__identity',)
    def username(self,obj):
        return obj.track.user.username
    def name(self,obj):
        return obj.track.name
    def identity(self,obj):
        return obj.track.identity.name
    username.short_description = '用户账户'
    name.short_description='姓名'
    identity.short_description="等级"
    
    
    
class TransactionhistoryAdmin(admin.ModelAdmin):
    '''交易记录'''
    list_display = ('__str__','memberlevel','type','io','price','overage','pay_by','remark','source_track_username','source_track_name','joined')
    search_fields = ('track__user__username','track__name','remark')
    list_filter = ('io','track__identity',)
    
    def source_track_name(self,obj):
        try:
            name = Doubletrack.objects.get(pk=obj.source_track).name
        except ObjectDoesNotExist:
            name = None
        return name
    
    def source_track_username(self,obj):
        try:
            username = Doubletrack.objects.get(pk=obj.source_track).user.username
        except ObjectDoesNotExist:
            username = None
        return username
    source_track_name.short_description = "交易引发源姓名"
    source_track_username.short_description = "交易引发源用户名"
    
class AwardsAdmin(admin.ModelAdmin):
    '''奖金类型'''
    list_display = ('name','memberlevel','percentage','layer_num','seniority_num')
    search_fields=('name',)
    list_filter = ('memberlevel',)
    
class WithdrawhistoryAdmin(admin.ModelAdmin):
    list_display = ('user','track_name','price','tax','fee','real_price','bank','bank_account','into_account','remark','joined','updated')
    list_filter = ('into_account',)
    
    def track_name(self,obj):
        return Doubletrack.objects.get(user=obj.user).name
    track_name.short_description = "姓名"
    
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name','price','integral','shoppingcoupons',)
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('ordercode','pay_by','totalquantity','totalprice','status','ship_recipient','ship_mobile','ship_address','joined','updated')
    list_filter = ('status',)
    search_fields=('ordercode','status','ordercode__ordercode')

class OrderdetailAdmin(admin.ModelAdmin):
    list_display = ('ordercode','goodsname','price','quantity','supplier','joined')
    search_fields = ('goodsname','ordercode__ordercode')

admin.site.register(Orderdetail,OrderdetailAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Withdrawhistory,WithdrawhistoryAdmin)
admin.site.register(Doubletrack,DoubletrackAdmin)
admin.site.register(Memberlevel,MemberlevelAdmin)
admin.site.register(Bonus,BonusAdmin)
admin.site.register(Transactionhistory,TransactionhistoryAdmin)
admin.site.register(Awards,AwardsAdmin)
