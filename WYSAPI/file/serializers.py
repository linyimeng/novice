'''
Created on 2016-12-5
@author: yimeng
'''
from rest_framework.serializers import ModelSerializer
from file.models import Images

class ImgSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ('img','type','creator')