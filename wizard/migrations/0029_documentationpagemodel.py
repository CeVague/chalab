# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0028_auto_20160830_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentationPageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
            ],
        ),
    ]
