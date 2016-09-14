# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0006_auto_20160827_1028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
