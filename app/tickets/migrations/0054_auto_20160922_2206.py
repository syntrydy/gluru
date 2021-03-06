# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-22 22:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0053_auto_20160920_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='priority',
        ),
        migrations.AddField(
            model_name='ticket',
            name='last_notification_sent',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 22, 22, 6, 1, 955400, tzinfo=utc), verbose_name='Last notification was sent'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='issue_type',
            field=models.CharField(choices=[(b'outage', 'Production Outage'), (b'impaired', 'Production Impaired'), (b'pre_production', 'Pre-Production Issue'), (b'minor', 'Minor Issue'), (b'new_development', 'New Development Issue')], default=b'', max_length=20, verbose_name='Issue type'),
        ),
    ]
