# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officers', '0008_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture_link',
            field=models.URLField(default='https://www.facebook.com/ucberkeleytsa/photos_stream?tab=photos_albums'),
            preserve_default=True,
        ),
    ]
