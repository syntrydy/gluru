# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-09 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0031_auto_20161207_1022'),
        ('tickets', '0061_auto_20161207_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='company_association',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='profiles.Company'),
        ),
    ]