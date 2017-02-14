'''
Created on 2017-2-3

@author: yimeng
'''
from django import forms

from goods.models import Goods

class GoodsForm(forms.ModelForm):
    
    class Meta:
        model = Goods
        fields = ['gsav','type'] 