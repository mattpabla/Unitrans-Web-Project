# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0003_shift_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='user_id',
            field=models.CharField(max_length=200),
        ),
    ]
