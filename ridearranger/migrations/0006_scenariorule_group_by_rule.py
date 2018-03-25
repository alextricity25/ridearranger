# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridearranger', '0005_auto_20180305_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenariorule',
            name='group_by_rule',
            field=models.CharField(choices=[('DT', 'Destination Location'), ('SR', 'Source Location')], default='blah', max_length=20),
            preserve_default=False,
        ),
    ]