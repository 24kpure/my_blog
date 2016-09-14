#!/usr/bin/env python
# coding=utf-8
from django.db import models


# coding:utf-8

# Create your models here.

class Article(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(u'title', max_length=60)
    content = models.TextField(u'content')
    author = models.CharField(u'author', max_length=50)
    abstract = models.CharField(max_length=54, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    topped = models.BooleanField(default=False)
    pub_date = models.DateField(u'time-public', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'update_time', auto_now=True)
    state = models.CharField(u'state', max_length=2)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        info = self.title + "----" + self.author
        return info


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    pub_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    userName = models.CharField(max_length=50)
    content = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.content[:20]


class Collections(models.Model):
    userId = models.CharField(max_length=50);
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)
    status = models.CharField(u'state', max_length=2)

    def __unicode__(self):
        return "user=" + self.userId + " article=" + self.article_id + " status=" + self.status


class Joke(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=50)

    def __unicode__(self):
        return self.content
