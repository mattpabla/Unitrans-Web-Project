# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0005_shift_coverer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='coverer',
        ),
        migrations.AddField(
            model_name='shift',
            name='covered',
            field=models.BooleanField(default=False),
        ),
    ]
