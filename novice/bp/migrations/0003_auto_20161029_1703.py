# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0002_company_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=225, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='personal',
            name='remark',
            field=models.TextField(null=True, blank=True),
        ),
    ]
