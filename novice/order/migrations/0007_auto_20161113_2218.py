# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20161113_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='price',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='productiondate',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='validity',
        ),
    ]
