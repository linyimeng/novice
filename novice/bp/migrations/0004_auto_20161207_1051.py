# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0003_auto_20161029_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='imgurl',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='imgurl',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
