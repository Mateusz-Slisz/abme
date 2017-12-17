# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-17 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171215_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serial',
            old_name='creator',
            new_name='creators',
        ),
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.AddField(
            model_name='film',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='film_director', to='api.Person'),
        ),
    ]
