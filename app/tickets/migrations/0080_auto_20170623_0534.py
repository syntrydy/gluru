# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-23 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0079_auto_20170622_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='product',
            field=models.CharField(choices=[(b'', b'Select a Product'), (b'GLUU', b'Gluu Server'), (b'OXD', b'OXD'), (b'SUP_GLUU', b'Super Gluu'), (b'CLUSTER', b'Cluster Manager')], default=b'N/A', max_length=10, verbose_name='Product'),
        ),
    ]
