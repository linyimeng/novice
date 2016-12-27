# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_detail_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='company',
            field=models.ForeignKey(to='bp.Company', null=True, blank=True),
        ),
    ]
