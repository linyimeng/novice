from django.contrib import admin
from goods.models import Goods,Type,TypeAttr
# Register your models here.
admin.site.register(Goods)
admin.site.register(Type)
admin.site.register(TypeAttr)