from django.contrib import admin
from file.models import Images
# Register your models here.
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('__str__','type','creator','joined','updated')
    
admin.site.register(Images,ImagesAdmin)