# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20161120_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('N', 'Not reviewed'), ('R', 'Reviewed'), ('P', 'pay'), ('W', 'wait ship'), ('T', 'In transit'), ('D', 'Delivered'), ('I', 'Invoiced'), ('R', 'Return goods'), ('O', 'end')], default='N', max_length=10),
        ),
    ]
