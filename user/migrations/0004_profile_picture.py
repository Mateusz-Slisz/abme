# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='photos/default.png', upload_to='photos/'),
        ),
    ]
