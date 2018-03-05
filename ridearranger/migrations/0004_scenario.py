# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridearranger', '0003_auto_20180305_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_location_rule', models.CharField(choices=[('HL', 'Home Location'), ('SL', 'Same Location')], max_length=20)),
                ('dest_location_rule', models.CharField(choices=[('HL', 'Home Location'), ('SL', 'Same Location')], max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
