# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20161106_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='batch',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
