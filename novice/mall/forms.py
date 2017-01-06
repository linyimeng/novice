'''
Created on 2017-1-6

@author: yimeng
'''

from django.forms import ModelForm
from mall.models import Shippingaddress

class ShippingaddressForm(ModelForm):
    class Meta:
        model = Shippingaddress
        fields = ['user','recipient','mobile','city','province','county','address','is_default']
        
    def clean_is_default(self):
        is_default = self.cleaned_data['is_default']
        user = self.cleaned_data['user']
        if is_default:
            Shippingaddress.objects.filter(user=user).update(is_default=False)
        return is_default
        