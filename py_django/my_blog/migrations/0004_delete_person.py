# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_auto_20160827_1022'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
