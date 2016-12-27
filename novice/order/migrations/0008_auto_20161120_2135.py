# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20161113_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='price',
            field=models.DecimalField(default=1, decimal_places=8, max_digits=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='quantity',
            field=models.DecimalField(default=1, decimal_places=2, max_digits=10),
            preserve_default=False,
        ),
    ]
