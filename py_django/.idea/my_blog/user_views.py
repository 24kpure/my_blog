#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import Article, Category, Collections
from my_tools import next_id
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView


def haslog(request):
    result = True
    if not request.user.is_authenticated():
        result = False
    return result


def home(request):
    return render(request, 'home.html', {'art': art(request)})


def allart(request):
    article = Article.objects.filter(state='1').order_by('-update_time')[:8]
    return article


def my_login(request):
    # User.objects.create(userId=my_tools.next_id(), username='lmj', password='vae.',last_login="2015-5-8")
    info = ''
    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        # user = User.objects.filter(username=name, password=pwd)
        user = authenticate(username=name, password=pwd)
        if user is not None:
            if user.is_active:
                # print user.is_active
                login(request, user)
                return render(request, 'home.html', {'art': allart(request)})
        else:
            info = u"用户名或密码错误"
    return render(request, "login.html", {'info': info})


def my_logout(request):
    if haslog(request):
        logout(request)
    article_list = Article.objects.filter(state='1')
    return render(request, 'home.html', {'art': article_list})


def register(request):
    if request.method != 'POST':
        return render(request, "register.html")
    else:
        info = "注册成功"
        name = request.POST['username']
        pwd = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.get(username=name)
            info = "该用户名已存在"
        except ObjectDoesNotExist:
            user = User.objects.create_user(name, email, pwd)
            user.save()
            user = authenticate(username=name, password=pwd)
            login(request, user)
            article_list = Article.objects.filter(state='1')
            return render(request, 'home.html', {'art': article_list})
        return render(request, "register.html", {"info": info})


def user_info(request):
    article = Article.objects.filter(author=request.user.username).order_by('state', '-update_time')
    collections = Collections.objects.filter(userId=request.user.id, status='1')
    category_list = Category.objects.all().order_by('id')
    return render(request, 'user_info.html',
                  {'art': article, 'collections': collections, 'category_list': category_list})


class IndexView(ListView):
    template_name = "home.html"
    context_object_name = "art"

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）

    def get_queryset(self):
        article_list = Article.objects.filter(state='1').order_by('-update_time')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('id')
        return super(IndexView, self).get_context_data(**kwargs)
