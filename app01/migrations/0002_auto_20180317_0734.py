# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-17 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='m',
        ),
        migrations.AddField(
            model_name='classes',
            name='m',
            field=models.ManyToManyField(to='app01.Teachers'),
        ),
    ]