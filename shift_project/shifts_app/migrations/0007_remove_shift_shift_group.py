# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0006_auto_20180718_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='shift_group',
        ),
    ]
