# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-17 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u540d\u79f0'),
        ),
    ]