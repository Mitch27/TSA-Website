# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('grad_year', models.IntegerField()),
                ('description', models.TextField()),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]