# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_auto_20160310_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='dispatcher_task_id',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
