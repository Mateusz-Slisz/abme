# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_bookreadlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookReadlist',
            new_name='BookWatchlist',
        ),
    ]
