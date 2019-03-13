# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0007_auto_20160326_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('picture', models.ImageField(default='sponsor/circus.png', upload_to='sponsor/')),
                ('ordering', models.IntegerField()),
                ('link', models.URLField()),
            ],
        ),
    ]
