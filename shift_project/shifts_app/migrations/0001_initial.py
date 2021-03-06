# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0, blank=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ShiftGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_datetime', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('end_datetime', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='shift',
            name='shift_group',
            field=models.ForeignKey(related_name='shifts_related', to='shifts_app.ShiftGroup'),
        ),
        migrations.AddField(
            model_name='run',
            name='shift',
            field=models.ForeignKey(related_name='runs_related', to='shifts_app.Shift'),
        ),
    ]
