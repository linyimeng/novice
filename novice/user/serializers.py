'''
Created on 2016-9-18

@author: yimeng
'''
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from staff.models import EmpInfo
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')
    eid = serializers.SerializerMethodField()
    class Meta:
        model = Token
        fields = ("auth_token",'user','eid')
    
    def get_eid(self,obj):
        eid = EmpInfo.objects.get(user__pk=obj.user.pk).pk
        return eid;
        
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(min_length=6,max_length=128,write_only=True)
    email = serializers.EmailField()
    pk = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ('pk','username','email')
