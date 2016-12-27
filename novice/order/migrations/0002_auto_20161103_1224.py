# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='price',
            field=models.DecimalField(decimal_places=8, max_digits=18),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalprice',
            field=models.DecimalField(decimal_places=8, max_digits=18),
        ),
    ]
