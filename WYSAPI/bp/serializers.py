'''
Created on 2016-10-4

@author: yimeng
'''
from rest_framework import serializers
from bp.models import Company,Personal

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
                  'pk',
                  'name',
                  'is_vendor',
                  'is_client',
                  'landline',
                  'phone',
                  'email',
                  'fax',
                  'address',
                  'remark',
                 )
        
class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields=('pk','name','user','company','address','landline','phone','email','fax')