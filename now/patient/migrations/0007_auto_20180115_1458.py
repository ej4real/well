# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20180114_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
