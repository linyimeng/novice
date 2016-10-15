from django.contrib import admin
from blog.models import BlogUser,Article,Comment
# Register your models here.
admin.site.register(BlogUser)
admin.site.register(Article)
admin.site.register(Comment)
