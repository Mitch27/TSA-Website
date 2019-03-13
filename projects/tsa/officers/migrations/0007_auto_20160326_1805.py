# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0006_auto_20160326_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(default='event_pics/circus.png', upload_to='event_pics/'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='picture',
            field=models.ImageField(default='event_pics/circus.png', upload_to='officer_pics/'),
        ),
    ]