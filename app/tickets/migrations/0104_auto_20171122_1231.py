# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-22 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import tickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0103_auto_20171122_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketdocuments',
            name='file',
            field=models.FileField(blank=True, max_length=255, upload_to=tickets.models.ticket_file_path),
        ),
    ]
