# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_goods_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeattr',
            name='logicname',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='typeattr',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
