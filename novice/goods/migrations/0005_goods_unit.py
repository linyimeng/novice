# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20161029_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='unit',
            field=models.CharField(max_length=10, blank=True, null=True),
        ),
    ]
