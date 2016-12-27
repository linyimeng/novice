# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20161112_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(default=1, to='goods.Type'),
            preserve_default=False,
        ),
    ]
