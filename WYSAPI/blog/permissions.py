'''
Created on 2016-10-1

@author: yimeng
'''
from rest_framework.permissions import BasePermission

class UserIsOwnerBlog(BasePermission):
    '''
    判断该用户是不是该博客内容的拥有者
    '''
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id