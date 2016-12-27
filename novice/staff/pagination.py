'''
Created on 2016-10-25

@author: yimeng
'''
from rest_framework.pagination import LimitOffsetPagination #其他系统分页类：PageNumberPagination

class StaffLimitOffsetPagination(LimitOffsetPagination):
    #最大每页个数
    max_limit = 10