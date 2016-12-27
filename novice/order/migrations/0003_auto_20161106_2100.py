# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20161103_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='productiondate',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='validity',
            field=models.DateField(null=True, blank=True),
        ),
    ]
