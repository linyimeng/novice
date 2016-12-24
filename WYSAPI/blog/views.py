'''
Created on 2016-11-10

@author: yimeng
'''
from blog.models import Article,Comment
from django.shortcuts import render
from blog.forms import CommentForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
def loginx(request):
    if request.method=="GET":
        print(request.GET.get('next',''))
        return render(request,'login.html',{
                'next':request.GET.get('next',''),
                'app_path':'accounts/login/',
                'form':LoginForm,
                'title':'登录',
                'content_title':'登录',
               })
    else:
        userform = LoginForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(request.POST.get('next','/blog/'))
        return render(request, 'blog/login.html', {
                        'next':request.POST.get('next','/blog/'),
                        'app_path':'accounts/login/',
                        'form':LoginForm,
                        'title':'登录',
                        'content_title':'登录',
                        'is_authenticated':True,
                      })
        
def article_list(request):
    article_list = Article.objects.filter(published=True).values('pk','title','author','updated','description').order_by('-updated')
    return render(request,'blog/article_list.html',{'articles':article_list})


def article_detail(request,pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article__pk=pk)
    return render( request,'blog/article_detail.html',
                   {
                    'article':article,
                    'comments':comments,
                    'commentform':CommentForm({'article':pk})
                   } 
                 )
@login_required
def comment_create(request,apk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            content = form.cleaned_data['content']
            article = form.cleaned_data['article']
            Comment.objects.create(user=user,content=content,article_id=article)
            return render(request,'blog/ok_or_fail.html',{'info':'评论或提问成功','apk':apk })
        else:
            return render(request,'blog/ok_or_fail.html',{'info':'评论或提问失败！！！','apk':apk })
    else:
        article_url = '/blog/article/' + str(apk) + '/'
        return HttpResponseRedirect(article_url)
    
    
    
    
    