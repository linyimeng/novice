# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20161112_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='typeattr',
            name='keyname',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='typeattr',
            name='type',
            field=models.CharField(default='s', choices=[('s', 'static'), ('d', 'dynamic'), ('ss', 'system_static'), ('sd', 'system_dynamic')], max_length=2),
        ),
    ]
