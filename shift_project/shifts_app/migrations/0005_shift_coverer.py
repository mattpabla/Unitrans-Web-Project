# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0004_auto_20180717_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='coverer',
            field=models.CharField(default=b'None', max_length=200),
        ),
    ]
