# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0010_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('author', models.CharField(max_length=50, verbose_name='author')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='time-public')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time')),
            ],
        ),
    ]
