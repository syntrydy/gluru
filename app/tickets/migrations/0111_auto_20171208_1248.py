# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-08 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0110_auto_20171208_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gluuticket',
            name='set_default_gluu',
        ),
        migrations.AddField(
            model_name='ticket',
            name='set_default_gluu',
            field=models.BooleanField(default=False, verbose_name='Default Gluu'),
        ),
    ]
