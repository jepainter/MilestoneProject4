# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-10 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20200103_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='owner_id',
            field=models.CharField(default='1', max_length=10),
        ),
    ]