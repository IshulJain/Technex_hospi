# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-05 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_auto_20170204_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chutiyapa',
            name='fieldChutiyap',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='startupfair',
            name='description',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]
