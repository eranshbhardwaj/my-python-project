# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-26 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0008_auto_20180722_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='type',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=50),
        ),
    ]
