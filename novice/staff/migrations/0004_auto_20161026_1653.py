# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20161026_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empinfo',
            name='customid',
            field=models.CharField(blank=True, null=True, max_length=30),
        ),
    ]
