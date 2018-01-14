# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 16:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_name', models.CharField(max_length=255, null=True, unique=True)),
                ('pat_email', models.EmailField(max_length=255, null=True, unique=True)),
                ('pat_address1', models.CharField(max_length=255, null=True)),
                ('pat_age', models.CharField(max_length=3, null=True)),
                ('pat_birthdate', models.DateField(null=True)),
                ('gender_check', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('cont_num', models.IntegerField(max_length=11, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
