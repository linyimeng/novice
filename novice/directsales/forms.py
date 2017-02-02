'''
Created on 2017-1-14

@author: yimeng
'''
from django.forms import ModelForm
from directsales.models import Doubletrack



class DoubletrackForm(ModelForm):
    
    class Meta:
        model = Doubletrack
        fields = ['user','parent','isright','identity','directpushuser','name','phone','address','bank','bank_account','pay_password']