'''
Created on 2016-11-10

@author: yimeng
'''
from django import forms

class CommentForm(forms.Form):
    user = forms.CharField(max_length=30,label='姓名',required=True)
    content = forms.CharField(label='评论或提问内容',widget=forms.Textarea,required=True)
    article = forms.IntegerField(widget=forms.HiddenInput)
    