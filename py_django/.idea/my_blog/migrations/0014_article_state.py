# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0013_auto_20160829_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='state',
            field=models.CharField(default=1, max_length=2, verbose_name='state'),
            preserve_default=False,
        ),
    ]
