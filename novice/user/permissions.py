'''
Created on 2016-10-1

@author: yimeng
'''
from rest_framework.permissions import BasePermission

class UserIsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id