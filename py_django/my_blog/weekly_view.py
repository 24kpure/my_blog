#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import Article, Category, Collections, Comment
from my_tools import next_id
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView
from django.db.models import Count
from django.http import HttpResponseRedirect


class IndexView(ListView):
    template_name = "datepicker.html"
    context_object_name = "art"

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）

    def get_queryset(self):
        article_list = Article.objects.filter(state='1').order_by('-update_time')
        return article_list


class Test(ListView):
    template_name = "test.html"
    context_object_name = "art"

    def get_queryset(self):
        article_list = Article.objects.filter(state='1').order_by('-update_time')
        return article_list


def tiaozhuan(request):
    if request.method == 'GET':
        url = request.GET['url']
        # url ='https://' + url
        print url
    return HttpResponseRedirect(url)
