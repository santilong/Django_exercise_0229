# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-19 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20180317_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='m',
            field=models.ManyToManyField(related_name='sssss', to='app01.Teachers'),
        ),
    ]
