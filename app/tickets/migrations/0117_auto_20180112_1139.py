# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-01-12 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0116_auto_20171211_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketproduct',
            name='product',
            field=models.CharField(blank=True, choices=[(b'', b'Select a Product'), (b'Oxd', b'OXD'), (b'Super Gluu', b'Super Gluu'), (b'Cluster', b'Cluster Manager')], default=b'', max_length=20, verbose_name='Product'),
        ),
    ]
