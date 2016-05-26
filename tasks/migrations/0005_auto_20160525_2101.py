# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(null=True, to='tasks.Label'),
        ),
    ]
