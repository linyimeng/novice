'''
Created on 2016-11-10

@author: yimeng
'''
from blog.models import Article,Comment
from django.shortcuts import render
from blog.forms import CommentForm

def article_list(request):
    article_list = Article.objects.filter(published=True).values('pk','title','author','joined').order_by('updated')
    return render(request,'article_list.html',{'articles':article_list})


def article_detail(request,pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article__pk=pk)
    return render( request,'article_detail.html',
                   {
                    'article':article,
                    'comments':comments,
                    'commentform':CommentForm({'article':pk})
                   } 
                 )
    
def comment_create(request,apk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            content = form.cleaned_data['content']
            article = form.cleaned_data['article']
            Comment.objects.create(user=user,content=content,article_id=article)
            return render(request,'ok_or_fail.html',{'info':'评论或提问成功','apk':apk })
        else:
            return render(request,'ok_or_fail.html',{'info':'评论或提问失败！！！','apk':apk })
        
            
    
    
    
    
    