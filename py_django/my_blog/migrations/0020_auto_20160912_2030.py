# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0019_joke'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='update_time',
        ),
        migrations.AddField(
            model_name='category',
            name='introduce',
            field=models.CharField(default=datetime.datetime(2016, 9, 12, 12, 30, 25, 618000, tzinfo=utc), max_length=120, verbose_name=b'\xe4\xbb\x8b\xe7\xbb\x8d'),
            preserve_default=False,
        ),
    ]
