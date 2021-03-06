# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-01 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0065_auto_20170501_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketnotification',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticketnotification',
            name='is_txt_sent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
