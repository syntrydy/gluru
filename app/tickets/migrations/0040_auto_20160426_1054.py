# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0039_auto_20160426_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='os_type',
            field=models.BooleanField(default=False, verbose_name='Is it 64-bit hardware?'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ram',
            field=models.BooleanField(default=False, verbose_name='Does the server have at least 4GB RAM?'),
        ),
    ]