from django.contrib import admin
from directsales.models import Doubletrack,Memberlevel,Bonus,Transactionhistory,Awards
# Register your models here.
class DoubletrackAdmin(admin.ModelAdmin):
    list_display = ('pk','user','name','identity','parent','isright','directpushuser','phone','joined','updated')
    
class MemberlevelAdmin(admin.ModelAdmin):
    list_display = ('__str__','price','joined')
    
class BonusAdmin(admin.ModelAdmin):
    list_display = ('__str__','cash','integral','shoppingcoupons','updater','updated')
    
class TransactionhistoryAdmin(admin.ModelAdmin):
    list_display = ('__str__','memberlevel','type','io','price','overage','pay_by','remark','joined')
    
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('__str__','name','memberlevel','percentage')
    
admin.site.register(Doubletrack,DoubletrackAdmin)
admin.site.register(Memberlevel,MemberlevelAdmin)
admin.site.register(Bonus,BonusAdmin)
admin.site.register(Transactionhistory,TransactionhistoryAdmin)
admin.site.register(Awards,AwardsAdmin)
