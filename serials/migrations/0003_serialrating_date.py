# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0002_auto_20171116_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='serialrating',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
