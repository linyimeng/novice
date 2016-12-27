# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0006_auto_20161220_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, null=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, verbose_name='phone', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='email',
            field=models.EmailField(blank=True, null=True, max_length=254),
        ),
    ]
