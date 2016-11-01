#!/usr/bin/env python
# coding=utf-8
import re

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from models import Article, Category, Comment, Collections
from my_tools import next_id


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
        user_id = self.request.user.id
        context['comment'] = Comment.objects.filter(article=article)
        collections = Collections.objects.filter(article=article, userId=user_id)
        if collections.__len__() > 0:
            collection = int(collections[0].status)
        else:
            collection = int(0)
        context['collections'] = collection
        return context


class UpdateArticleDetail(ArticleDetailView):
    template_name = "edit_article.html"

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.filter().exclude(id=0).order_by('id')
        return super(ArticleDetailView, self).get_context_data(**kwargs)


@login_required(login_url='login.html')
def edit_article(request):
    if request.method != 'POST':
        # joke_length = Joke.objects.all().__sizeof__()
        # dic = {'joke1': Joke.objects.get(id=random.randint(1, joke_length)),
        #       'joke2': Joke.objects.get(id=random.randint(1, joke_length))}
        category_list = Category.objects.filter().exclude(id=0).order_by('id')
        return render(request, "edit_article.html", {'category_list': category_list})
    elif request.POST['aid']:
        aid = request.POST['aid']
        title = request.POST['title']
        content = request.POST['editor']
        state = request.POST['state']
        category = int(request.POST['category'])
        abstract = content
        dr = re.compile(r'<[^>]+>', re.S)
        abstract = dr.sub('', abstract)
        abstract = abstract[:6]
        Article.objects.filter(id=aid).update(title=title, content=content, state=state, abstract=abstract,
                                              category_id=category)
        # //article_list = Article.objects.filter(state='1').order_by('-update_time')
        # //category_list = Category.objects.filter().order_by('id')
        return HttpResponseRedirect('/')
    else:
        title = request.POST['title']
        content = request.POST['editor']
        state = request.POST['state']
        category = int(request.POST['category'])
        abstract = content
        dr = re.compile(r'<[^>]+>', re.S)
        abstract = dr.sub('', abstract)
        abstract = abstract[:6]
        article = Article(id=next_id(), author=request.user.username, content=content, title=title, state=state,
                          abstract=abstract, category_id=category)
        article.save()
        article_list = Article.objects.filter(state='1').order_by('-update_time')
        category_list = Category.objects.filter().order_by('id')
        return render(request, 'home.html', {'art': article_list, 'category_list': category_list})


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
    article = Article.objects.get(id=id)
    if Collections.objects.filter(article=article, userId=request.user.id).__len__() == 0:
        Collections.objects.create(article=article, userId=request.user.id, status=status)
    else:
        Collections.objects.filter(article=article, userId=request.user.id).update(status=status)
    article.likes=Collections.objects.filter(article=article, userId=request.user.id).__len__()
    article.save()
    info = '收藏本文'
    if status == '1':
        info = '取消收藏'
    dic = {"info": info}
    return JsonResponse(dic)


class CategoryArticle(ListView):
    template_name = "home.html"
    context_object_name = "category_list"

    def get_queryset(self):
        category_list = Category.objects.filter().exclude(id=0).order_by('id')
        return category_list

    def get_context_data(self, **kwargs):
        id = self.kwargs['category_id']
        art = Article.objects.filter(category=id).filter(state=1)
        results = Comment.objects.values('article__title', 'article__id', 'article__category__name').annotate(
            dcount=Count('article')).order_by(
            '-dcount')
        print results
        kwargs['max_comment'] = results
        kwargs['art'] = art
        kwargs['cate_id'] = int(id)
        return super(CategoryArticle, self).get_context_data(**kwargs)


# def art_search(request):
#     search = request.POST['search']
#     # author_article = Article.objects.filter(author__contains=search)
#     # title_article = Article.objects.filter(title__contains=search)
#     # content_article = Article.objects.filterQ(author__contains=search)
#     # art = author_article | title_article | content_article
#     art = Article.objects.filter(Q(author__contains=search) | Q(title__contains=search) | Q(content__contains=search) |
#                                  Q(category__name__icontains=search))
#     category_list = Category.objects.all()
#     return render(request, 'home.html', {'art': art, 'search': search, 'category_list': category_list})
class ArticleSearch(CategoryArticle):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        print self.request.method
        search = self.request.GET['search']
        # print 'search=', search
        art = Article.objects.filter(
            Q(author__contains=search) | Q(title__contains=search) | Q(content__contains=search) |
            Q(category__name__icontains=search)).filter(state=1)
        kwargs['art'] = art
        kwargs['search_url'] = "?search=" + search
        return super(CategoryArticle, self).get_context_data(**kwargs)
