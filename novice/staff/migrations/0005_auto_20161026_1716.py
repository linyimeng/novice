# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20161026_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empinfo',
            name='customid',
            field=models.CharField(null=True, blank=True, unique=True, max_length=30),
        ),
    ]
