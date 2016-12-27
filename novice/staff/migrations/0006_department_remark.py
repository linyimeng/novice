# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20161026_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='remark',
            field=models.TextField(null=True, blank=True),
        ),
    ]
