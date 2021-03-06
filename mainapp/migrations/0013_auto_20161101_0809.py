# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 08:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='u_education_end_year',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='u_education_start_year',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='u_github',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='u_linkedin',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
