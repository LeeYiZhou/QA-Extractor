# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-31 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doccon2', '0005_auto_20160731_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurations',
            name='name',
            field=models.CharField(max_length=180, verbose_name='Configuration Name'),
        ),
    ]
