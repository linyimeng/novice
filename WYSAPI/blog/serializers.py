from blog.models import BlogUser,Article,Comment
from rest_framework import serializers

class BlogUserSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields= ('id','user','nickname','blogname')

class ArticleSerializer(serializers.ModelSerializer):
    #author = serializers.HyperlinkedRelatedField('user-detail',read_only=True)
    class Meta:
        model = Article
        fields= ('id','title','author','description','content','joined','updated')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields= ('user','article','content')