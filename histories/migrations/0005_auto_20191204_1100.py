# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-04 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0004_remove_historyevent_artifact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyevent',
            name='event_era',
            field=models.CharField(choices=[('Gregorian', (('bc', 'BC'), ('ac', 'AC'))), ('Ages', (('bronze', 'Bronze Age'), ('iron', 'Iron Age'), ('middle', 'Middle Age'), ('atomic', 'Atomic Age'), ('space', 'Space Age'), ('information', 'Information Age')))], default='bc', max_length=50),
        ),
    ]
