# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-07 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0095_auto_20171107_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gluuticket',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='GluuTicket',
        ),
    ]
