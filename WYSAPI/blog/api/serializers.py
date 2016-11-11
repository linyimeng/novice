from blog.models import BlogUser,Article,Comment
from rest_framework import serializers

class BlogUserSerializer(serializers.ModelSerializer):
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
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    commen = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = (
                  'id',
                  'title',
                  'author',
                  'description',
                  'content',
                  'joined',
                  'updated',
                  'commen',
                 )
    def get_commen(self,obj):
        comment_set = Comment.objects.filter(article__pk=obj.id)
        commen = CommentSerializer(comment_set,many=True).data
        return commen