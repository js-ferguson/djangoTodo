# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-18 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='michael',
            field=models.BooleanField(default=True),
        ),
    ]
