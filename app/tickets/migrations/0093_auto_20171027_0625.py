# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-27 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0092_auto_20171026_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='GluuTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gluu_server_version', models.CharField(default=b'N/A', max_length=10, verbose_name='Gluu Server Version')),
                ('os_version', models.CharField(blank=True, choices=[(b'', b'Select Operating System'), (b'Ubuntu', b'Ubuntu'), (b'CentOS', b'CentOS'), (b'Rhel', b'RHEL'), (b'Debian', b'Debian')], max_length=8, null=True, verbose_name='Which OS are you using?')),
                ('os_version_name', models.FloatField(blank=True, null=True, verbose_name='OS Version')),
                ('date_added', models.DateTimeField(auto_now_add=True, help_text='Added date', verbose_name='Added')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='Modified date', verbose_name='Modified')),
            ],
        ),
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
        migrations.AlterField(
            model_name='ticketproduct',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ticket_id', to='tickets.Ticket'),
        ),
        migrations.AddField(
            model_name='gluuticket',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_id', to='tickets.Ticket'),
        ),
    ]