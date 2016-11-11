from blog.models import Article,Comment
from blog.api.serializers import ArticleSerializer,ArticleDetailSerializer,CommentSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
    
class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleDetailSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from datetime import datetime
# from django.http import Http404
# from rest_framework.generics import RetrieveUpdateAPIView
# from rest_framework.permissions import IsAuthenticated
# from blog.api.permissions import UserIsOwnerBlog 
# # Create your views here.
# 
# class BlogUserDetailAPIView(RetrieveUpdateAPIView):
#     '''
#     获取，更新用户信息
#     '''
#     serializer_class = BlogUserSerizlizer
#     queryset = BlogUser.objects.all()
#     permission_classes = (IsAuthenticated, UserIsOwnerBlog)
# 
# 
# @api_view(['GET'])
# def article_list(request,format=None):
#     if request.method == 'GET':
#         upk = request.user.id
#         authorid = BlogUser.objects.get(user__id = upk).id
#         article = Article.objects.filter(published=True,deleted=None,author__pk=authorid)
#         if not article:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ArticleSerializer(article,many=True,context={'request':request})
#         return Response(serializer.data)
#     
# @api_view(['GET'])
# def article_detail(request,pk,format=None):
#     if request.method == 'GET':
#         try:
#             article = Article.objects.get(pk=pk,published=True,deleted=None)
#         except Article.DoesNotExist:
#             return Response('article does not exist',status=status.HTTP_404_NOT_FOUND)
#         serializer = ArticleSerializer(article,context={'request': request})
#         return Response(serializer.data)
#     
# class UserDetail(APIView):
#     '''
#     get user detail
#     '''
#     def get(self,request,format=None):
#         upk = request.user.id;
#         authorid = BlogUser.objects.get(user__id = upk).id
#         try:
#             user = BlogUser.objects.get(pk=authorid,deleted=None)
#         except BlogUser.DoesNotExist:
#             return Response('user does not exist',status=status.HTTP_404_NOT_FOUND)
#         serializer = BlogUserSerizlizer(user,context={'request':request})
#         return Response(serializer.data)
# 
# 
# class CommentList(APIView):
#     '''
#     Show comments list related articles all Comment or create a comment
#     '''
#     def get(self,request,apk,format=None):
#         comment = Comment.objects.filter(article__id=apk,deleted=None)
#         print(comment)
#         if not comment:
#             return Response('no comment',status=status.HTTP_404_NOT_FOUND)
#         serializer = CommentSerializer(comment,many=True,context={'request':request})
#         return Response(serializer.data)
#     
#     def post(self,request,apk,format=None):
#         serializer = CommentSerializer(data=request.data,context={'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     
#     
# class CommentDetail(APIView):
#     '''
#     show a article all comment
#     '''
#     def get_object(self,pk):
#         try:
#             return Comment.objects.get(pk=pk,deleted=None)
#         except Comment.DoesNotExist:
#             raise Http404
#     
#     def put(self,request,pk,format=None):
#         comment = self.get_object(pk)
#         serializer = CommentSerializer(comment,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     
#     def delete(self,request,pk,format=None):
#         comment = self.get_object(pk)
#         comment.deleted = datetime.now()
#         comment.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     
    