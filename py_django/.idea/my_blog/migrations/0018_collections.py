# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0017_auto_20160904_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=2, verbose_name='state')),
                ('article', models.ForeignKey(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x89\x80\xe5\xb1\x9e\xe6\x96\x87\xe7\xab\xa0', to='my_blog.Article')),
            ],
        ),
    ]
