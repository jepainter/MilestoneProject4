# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-12 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0003_auto_20191212_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidlineitem',
            old_name='bid_id',
            new_name='bid_event',
        ),
    ]
