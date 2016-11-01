#!/usr/bin/env python
# coding=utf-8
"""py_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from my_blog import user_views
from my_blog import article_view
from my_blog import weekly_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # user
    url(r'^$', user_views.IndexView.as_view(), name='home'),
    url(r'^login', user_views.my_login, name='login'),
    url(r'^logout', user_views.my_logout, name='logout'),
    url(r'^register', user_views.register, name='register'),
    url(r'^user_info', user_views.user_info, name='user_info'),

    # article
    url(r'^article/(?P<article_id>\w+)$', article_view.ArticleDetailView.as_view(), name='article'),
    url(r'^edit_article', article_view.edit_article, name='edit_article'),
    url(r'^update_article/(?P<article_id>\w+)$', article_view.UpdateArticleDetail.as_view(), name='update_article'),
    url(r'^sub_comment$', article_view.sub_comment, name="sub_comment"),
    url(r'^art_collections$', article_view.art_collections, name="art_collections"),
    url(r'^art_search$', article_view.ArticleSearch.as_view(), name="art_search"),
    url(r'^category_article/(?P<category_id>\d+)$', article_view.CategoryArticle.as_view(), name="category_article"),


    url(r'^datepicker$',weekly_view.IndexView.as_view()),
    url(r'^test$',weekly_view.Test.as_view()),

]
