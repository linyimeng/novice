# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='superiors',
            field=models.ForeignKey(default=None, blank=True, null=True, to='goods.Type'),
        ),
    ]
