# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-23 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minis', '0005_auto_20170119_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniature',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
