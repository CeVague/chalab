# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0070_auto_20161120_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolmodel',
            name='dev_phase_description',
            field=models.TextField(default='Development phase: create models and submit them or directly submit results on validation and/or test data; feed-back are provided on the validation set only.', max_length=2048, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='protocolmodel',
            name='final_phase_description',
            field=models.TextField(default='Final phase: submissions from the previous phase are automatically cloned and used to compute the final score. The results on the test set will be revealed when the organizers make them available.', max_length=2048, verbose_name='Description'),
        ),
    ]
