# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20161026_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empinfo',
            name='entry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
