# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='shift_cover',
            field=models.BooleanField(default=False),
        ),
    ]
