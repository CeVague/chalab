# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0022_auto_20160828_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wizard.DatasetModel'),
        ),
    ]
