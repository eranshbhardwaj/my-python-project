# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0005_auto_20180721_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='image',
            field=models.ImageField(default='media/emp_images/icon.png', upload_to='media/emp_images/'),
        ),
    ]