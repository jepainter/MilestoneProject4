# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-02 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_category_description'),
        ('artifacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
    ]
