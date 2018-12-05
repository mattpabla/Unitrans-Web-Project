# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0002_shift_shift_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='user_id',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
