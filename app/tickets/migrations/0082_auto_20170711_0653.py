# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-11 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0081_auto_20170623_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='gluu_server_version',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='product',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='product_version',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='os_version',
            field=models.CharField(blank=True, choices=[(b'', b'Select Operating System'), (b'U1404', b'Ubuntu 14.04'), (b'CentOS65', b'CentOS 6.5'), (b'CentOS66', b'CentOS 6.6'), (b'CentOS67', b'CentOS 6.7'), (b'CentOS72', b'CentOS 7.2'), (b'Rhel65', b'RHEL 6.5'), (b'Rhel66', b'RHEL 6.6'), (b'Rhel67', b'RHEL 6.7'), (b'Rhel72', b'RHEL 7.2'), (b'Debian', b'Debian'), (b'Other', b'Other')], max_length=8, null=True, verbose_name='Which OS are you using?'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_category',
            field=models.CharField(choices=[(b'', b'Select a Category'), (b'OUTAGE', b'Outage'), (b'IDNTY', b'Identity Management'), (b'SSO', b'Single Sign-On'), (b'MFA', b'Authentication'), (b'AUT', b'Authorization'), (b'ACCESS', b'Access Management'), (b'CUSTOM', b'Customization'), (b'FEATURE', b'Feature Request'), (b'INSTALLATION', b'Installation'), (b'UPGRADE', b'Upgrade'), (b'MAINTENANCE', b'Maintenance'), (b'ADM', b'Administration'), (b'ENR', b'Enrollment'), (b'LOST', b'Lost Device'), (b'OTHER', b'Other')], max_length=20, verbose_name='Category'),
        ),
    ]