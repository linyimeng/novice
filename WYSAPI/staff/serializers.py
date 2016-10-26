'''
Created on 2016-9-20
@author: yimeng
'''
from rest_framework import serializers
from staff.models import Department,Jobs,EmpInfo

class DepartmentSerializer(serializers.ModelSerializer):
    staff_number = serializers.SerializerMethodField()
    superiors_name = serializers.SerializerMethodField()
    manager_name = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = (
                    'pk',
                    'name',
                    'superiors',
                    'manager',
                    'customid',
                    
                    'staff_number',
                    'superiors_name',
                    'manager_name',
                )
    def get_superiors_name(self,obj):
        if obj.superiors:
            return obj.superiors.name
        return None
    
    def get_staff_number(self,obj):
        staff_number = EmpInfo.objects.filter(department=obj.pk).count()
        return staff_number
    
    def get_manager_name(self,obj):
        if obj.manager:
            return obj.manager.name
        return None





class JobsSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()
    class Meta:
        model = Jobs
        fields = (
                  'pk',
                  'name',
                  'department',
                  
                  'department_name',
                 )
        
    def get_department_name(self,obj):
        if obj.department:
            return obj.department.name
        return None
    
    
class EmpInfoSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()
    job_name = serializers.SerializerMethodField()
    class Meta:
        model = EmpInfo
        fields= (
                 'pk',
                 'user',
                 'name',
                 'customid',
                 'department',
                 'job',
                 'work_address',
                 'office_phone',
                 'office_address',
                 'office_email',
                 'office_landline',
                 'cardid',
                 'bank_account',
                 'sex',
                 'marital_status',
                 'birthday',
                 'entry_time',
                 'isarchive',
                 
                 'department_name',
                 'job_name',
                 )
    
    def get_department_name(self,obj):
        if obj.department:
            return obj.department.name
        return None
    def get_job_name(self,obj):
        if obj.job:
            return obj.job.name
        return None