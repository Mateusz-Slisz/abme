# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_filmwatchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmrating',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
