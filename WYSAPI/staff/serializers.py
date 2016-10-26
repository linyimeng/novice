'''
Created on 2016-9-20
@author: yimeng
'''
from rest_framework import serializers
from staff.models import Department,Jobs,EmpInfo
from django.contrib.auth.models import User

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
    loginname = serializers.CharField(write_only=True)
    password = serializers.CharField(max_length=30,write_only=True)
    class Meta:
        model = EmpInfo
        fields= (
                 'pk',
                 'name',
                 'customid',
                 'department',
                 'job',
                 'work_address',
                 'office_phone',
                 'office_address',
                 'email',
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
                 
                 'loginname',
                 'password',
                 )
    
    def get_department_name(self,obj):
        if obj.department:
            return obj.department.name
        return None
    def get_job_name(self,obj):
        if obj.job:
            return obj.job.name
        return None
    def validate_loginname(self, value):
        user = User(username=value)
        if(user.is_authenticated()):
            raise serializers.ValidationError("loginname already exists")
        return value
    def create(self,validated_data):
        new_user = User(
                    email=validated_data['email'],
                    username=validated_data['loginname']
                )
        new_user.set_password(validated_data['password'])
        new_user.save()
        del validated_data['loginname']
        del validated_data['password']
        validated_data['user_id'] = new_user.pk
        empinfo = EmpInfo.objects.create(**validated_data)
        return empinfo
        
        