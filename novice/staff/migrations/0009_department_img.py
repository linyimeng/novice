# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20161101_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='img',
            field=models.ImageField(upload_to='department', blank=True, null=True),
        ),
    ]
