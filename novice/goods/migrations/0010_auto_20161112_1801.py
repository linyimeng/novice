# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import json
import django_pgjsonb.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_goods_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='sav',
            field=django_pgjsonb.fields.JSONField(decode_kwargs={'cls': json.dumps}, encode_kwargs={'cls': json.loads}),
        ),
    ]
