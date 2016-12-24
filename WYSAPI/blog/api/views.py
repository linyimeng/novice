from blog.models import Article
from blog.api.serializers import ArticleSerializer,ArticleDetailSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
    
class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleDetailSerializer