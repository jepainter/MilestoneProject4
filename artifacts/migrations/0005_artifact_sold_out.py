# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-06 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0004_auto_20191203_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='sold_out',
            field=models.BooleanField(default=False),
        ),
    ]
