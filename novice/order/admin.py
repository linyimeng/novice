from django.contrib import admin
from order.models import Order,Type,Detail
# Register your models here.
admin.site.register(Order)
admin.site.register(Type)
admin.site.register(Detail)