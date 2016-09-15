# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0018_collections'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
    ]
