# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 21:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_remove_invite_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 22, 21, 41, 23, 858747, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
    ]