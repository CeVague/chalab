# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0050_auto_20161020_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='metricmodel',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
