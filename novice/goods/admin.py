from django.contrib import admin
from goods.models import Goods,Type,TypeAttr


# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('__str__','type','gsav','updated','lastmodifyer','creator','joined')
    
class TypeAdmin(admin.ModelAdmin):
    list_display = ('__str__','name','superiors','updated','joined')
    
class TypeAttrAdmin(admin.ModelAdmin):
    list_display = ('__str__','keyname','goodstype','type')
    
admin.site.register(Goods,GoodsAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(TypeAttr,TypeAttrAdmin)