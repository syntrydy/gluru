# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-07 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0030_auto_20161121_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, default=b'', max_length=100, verbose_name='username'),
        ),
    ]