# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20161029_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='remark',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='specification',
            field=models.CharField(null=True, blank=True, max_length=30),
        ),
    ]
