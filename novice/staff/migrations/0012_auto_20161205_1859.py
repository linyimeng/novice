# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_auto_20161204_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='imgurl',
            field=models.CharField(blank=True, null=True, max_length=120),
        ),
    ]
