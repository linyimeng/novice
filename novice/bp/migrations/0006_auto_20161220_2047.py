# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0005_auto_20161220_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='is_job',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='job',
            field=models.CharField(null=True, blank=True, max_length=20),
        ),
    ]
