# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-19 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0075_auto_20170615_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='metricmodel',
            name='code',
            field=models.TextField(null=True),
        ),
    ]
