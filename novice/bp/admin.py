from django.contrib import admin
from bp.models import Company,Personal
# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name','company','job','is_job','phone','remark','joined','updated')


admin.site.register(Company)
admin.site.register(Personal,PersonalAdmin)