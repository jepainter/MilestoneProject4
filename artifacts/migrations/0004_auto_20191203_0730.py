# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-03 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0003_auto_20191203_0726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifact',
            old_name='category_id',
            new_name='category',
        ),
    ]