# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_pgjsonb.fields
import django.core.serializers.json


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20161112_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='sav',
        ),
        migrations.AddField(
            model_name='goods',
            name='gsav',
            field=django_pgjsonb.fields.JSONField(default={'a': 1}, decode_kwargs={}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}),
            preserve_default=False,
        ),
    ]
