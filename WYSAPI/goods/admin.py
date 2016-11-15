from django.contrib import admin
from goods.models import Goods,Type,TypeAttr
# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('__str__','type','gsav','updated','lastmodifyer','creator','joined')
admin.site.register(Goods,GoodsAdmin)
admin.site.register(Type)
admin.site.register(TypeAttr)
