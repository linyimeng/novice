# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_auto_20161205_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='empinfo',
            name='imgurl',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
