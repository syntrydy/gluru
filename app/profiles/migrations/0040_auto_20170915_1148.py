# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-15 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0039_auto_20170915_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitlements',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='entitlements',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='updated_at'),
        ),
    ]