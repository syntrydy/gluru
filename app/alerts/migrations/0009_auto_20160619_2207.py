# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0008_auto_20160426_1045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Alert',
        ),
        migrations.DeleteModel(
            name='AlertOption',
        ),
        migrations.RemoveField(
            model_name='emailsent',
            name='email',
        ),
        migrations.RemoveField(
            model_name='emailsent',
            name='subject',
        ),
    ]
