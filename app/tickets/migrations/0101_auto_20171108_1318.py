# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-08 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0100_auto_20171108_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='set_default_gluu',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='set_default_product',
        ),
    ]
