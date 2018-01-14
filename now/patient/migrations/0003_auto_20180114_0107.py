# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20180114_0043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientprofile',
            old_name='pat_address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='patientprofile',
            old_name='pat_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='patientprofile',
            old_name='pat_birthdate',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='patientprofile',
            old_name='cont_num',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='patientprofile',
            old_name='pat_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='patientprofile',
            old_name='gender_check',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='patientprofile',
            old_name='pat_name',
            new_name='name',
        ),
    ]
