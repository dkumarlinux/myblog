# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-05 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
