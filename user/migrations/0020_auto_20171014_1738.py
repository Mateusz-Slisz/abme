# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20171014_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='books',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bread',
            field=models.ManyToManyField(to='user.Bread'),
        ),
    ]