'''
Created on 2016-9-20

@author: yimeng
'''
from rest_framework import serializers
from staff.models import Department,Jobs,EmpInfo

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('pk','name','superiors','manager','customid')
        

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('pk','name','department')
        
        
class EmpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpInfo
        fields= ('pk','user','name','customid','department','job','work_address','office_phone',
                 'office_address','office_email','office_landline','cardid','bank_account',
                 'sex','marital_status','birthday','entry_time','isarchive'
                 )