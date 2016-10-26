from django.contrib import admin
from staff.models import Department,Jobs,EmpInfo
# Register your models here.
admin.site.register(Department)
admin.site.register(Jobs)
admin.site.register(EmpInfo)