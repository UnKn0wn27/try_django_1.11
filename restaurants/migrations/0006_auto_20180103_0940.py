# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-03 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_resturantlocation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='resturantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
