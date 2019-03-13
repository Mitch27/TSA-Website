# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 00:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0005_auto_20160326_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('event_date', models.DateField(default=datetime.date.today)),
                ('picture', models.ImageField(default='circus.png', upload_to='officer_pics/')),
                ('facebook_link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]