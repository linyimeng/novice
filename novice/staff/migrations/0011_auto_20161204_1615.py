# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_auto_20161204_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='imgurl',
            field=models.ImageField(null=True, blank=True, upload_to='department'),
        ),
    ]
