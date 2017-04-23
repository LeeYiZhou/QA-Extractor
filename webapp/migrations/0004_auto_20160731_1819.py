# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-31 12:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doccon2', '0003_auto_20160624_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurations',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 31, 12, 48, 57, 626000, tzinfo=utc), verbose_name='Date Added'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extractedanswers',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 31, 12, 49, 4, 636000, tzinfo=utc), verbose_name='Date Added'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toconvert',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 31, 12, 49, 14, 362000, tzinfo=utc), verbose_name='Date Added'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='configurations',
            name='description',
            field=models.CharField(max_length=400, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='converted',
            name='config_used',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doccon2.Configurations'),
        ),
        migrations.AlterField(
            model_name='converted',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Added'),
        ),
        migrations.RemoveField(
            model_name='converted',
            name='extracted',
        ),
        migrations.AddField(
            model_name='converted',
            name='extracted',
            field=models.ManyToManyField(blank=True, default=None, to='doccon2.extractedAnswers'),
        ),
        migrations.AlterField(
            model_name='extractedanswers',
            name='extracted_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doccon2.Converted'),
        ),
        migrations.AlterField(
            model_name='extractedanswers',
            name='solr_added',
            field=models.BooleanField(default=False),
        ),
    ]
