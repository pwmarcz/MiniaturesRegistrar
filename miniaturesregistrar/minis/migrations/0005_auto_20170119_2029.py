# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minis', '0004_auto_20170118_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='miniature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='minis.Miniature'),
        ),
        migrations.AlterField(
            model_name='element',
            name='number',
            field=models.IntegerField(choices=[(1, 'Skin'), (2, 'Weapon_wood'), (3, 'Eyes'), (4, 'Armor'), (5, 'Weapon_steel'), (6, 'Clothes_upper'), (7, 'Clothes_lower'), (8, 'Boots'), (9, 'Golden_elements'), (10, 'Bone_elements'), (11, 'Base')]),
        ),
    ]