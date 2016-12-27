# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.serializers.json
import django_pgjsonb.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0003_auto_20161029_1703'),
        ('order', '0005_auto_20161108_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='dynamic_attr',
        ),
        migrations.AddField(
            model_name='detail',
            name='gdav',
            field=django_pgjsonb.fields.JSONField(default={'a': 1}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='gsav',
            field=django_pgjsonb.fields.JSONField(default={'a': 1}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='personal',
            field=models.ForeignKey(blank=True, to='bp.Personal', null=True),
        ),
    ]
