from django.contrib import admin
from order.models import Order,Type,Detail
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__','type','status','totalprice','totalquantity','company','personal',
                    'recipient','phone','address','joined','creator','pk')

class DetailAdmin(admin.ModelAdmin):
    list_display = ('goods','quantity','price','gsav','gdav','joined','updated','pk')
    
    
class TypeAdmin(admin.ModelAdmin):
    list_display = ('__str__','io','pk')

admin.site.register(Order,OrderAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Detail,DetailAdmin)