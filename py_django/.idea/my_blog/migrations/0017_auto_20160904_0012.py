# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0016_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='userId',
            new_name='id',
        ),
    ]
