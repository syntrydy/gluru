# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-07 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0098_remove_answer_message_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='gluu_server_version',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='os_version',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='os_version_name',
        ),
    ]
