#!/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
from models import Article, Category, Comment, Collections, Joke
from my_tools import next_id
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import JsonResponse
import user_views
import random
import re

# def show_article(request):
#     art_id = request.GET['id']
#     article = Article.objects.filter(id=art_id)[0]
#     # print "art=",art.content
#     return render(request, "article.html", {"art": article})


class ArticleDetailView(DetailView):
    template_name = "article.html"
    context_object_name = "art"
    model = Article
    pk_url_kwarg = 'article_id'

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        article = super(ArticleDetailView, self).get_object()
        # print 'id=', super(ArticleDetailView, self).options()
        context['comment'] = Comment.objects.filter(article=article)
        # context['collections'] = Collections.objects.filter(article=article)[0]
        return context


class UpdateArticleDetail(ArticleDetailView):
    template_name = "edit_article.html"

    def get_context_data(self, **kwargs):
        joke = super(ArticleDetailView, self).get_context_data(**kwargs)
        #joke_length = Joke.objects.all.count()
        #joke['joke1'] = Joke.objects.get(id=random.randint(1, joke_length))
        #joke['joke2'] = Joke.objects.get(id=random.randint(1, joke_length))
        #print joke['joke1'], joke['joke2']
        return joke


@login_required(login_url='login.html')
def edit_article(request):
    if request.method != 'POST':
       # joke_length = Joke.objects.all().__sizeof__()
       # dic = {'joke1': Joke.objects.get(id=random.randint(1, joke_length)),
        #       'joke2': Joke.objects.get(id=random.randint(1, joke_length))}
        return render(request, "edit_article.html")
    elif request.POST['aid']:
        aid = request.POST['aid']
        title = request.POST['title']
        content = request.POST['editor']
        state = request.POST['state']
        abstract = content
	dr = re.compile(r'<[^>]+>', re.S)
        abstract = dr.sub('', abstract)
	abstract=abstract[:6]
        Article.objects.filter(id=aid).update(title=title, content=content, state=state, abstract=abstract)
        article_list = Article.objects.filter(state='1')
        return render(request, 'home.html', {'art': article_list})
    else:
        title = request.POST['title']
        content = request.POST['editor']
        state = request.POST['state']
        abstract = content
	dr = re.compile(r'<[^>]+>', re.S)
        abstract = dr.sub('', abstract)
	abstract=abstract[:6]
        article = Article(id=next_id(), author=request.user.username, content=content, title=title, state=state,
                          abstract=abstract)
        article.save()
        article_list = Article.objects.filter(state='1')
        return render(request, 'home.html', {'art': article_list})


@login_required(login_url='login.html')
def sub_comment(request):
    content = request.GET['content']
    id = request.GET['id']
    article = Article.objects.get(id=id);
    comment = Comment(id=next_id(), userName=request.user.username, content=content, article=article)
    comment.save()
    dic = {'info': "评论成功"}
    return JsonResponse(dic)


@login_required(login_url='login.html')
def art_collections(request):
    status = request.GET['status']
    id = request.GET['id']
    article = Article.objects.get(id=id);
    if Collections.objects.filter(article=article, userId=request.user.id).__len__() == 0:
        Collections.objects.create(article=article, userId=request.user.id, status=status)
    else:
        Collections.objects.filter(article=article, userId=request.user.id).update(status=status)
    info = '收藏本文'
    if status == '1':
        info = '取消收藏'
    dic = {"info": info}
    return JsonResponse(dic)


def art_search(request):
    search = request.POST['search']
    # author_article = Article.objects.filter(author__contains=search)
    # title_article = Article.objects.filter(title__contains=search)
    # content_article = Article.objects.filterQ(author__contains=search)
    # art = author_article | title_article | content_article
    art = Article.objects.filter(Q(author__contains=search) | Q(title__contains=search) | Q(content__contains=search))
    return render(request, 'home.html', {'art': art, 'search': search})


class Search(ListView):
    template_name = "home.html"
    context_object_name = "art"

    def get_queryset(self, request):
        search = request.POST['search']
        print search
        art = Article.objects.filter(
            Q(author__contains=search) | Q(title__contains=search) | Q(content__contains=search))
        return art
