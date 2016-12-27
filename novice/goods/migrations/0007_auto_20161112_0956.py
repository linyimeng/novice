# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_pgjsonb.fields
import django.core.serializers.json


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20161029_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeattr',
            old_name='logicname',
            new_name='keyname',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='costprice',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='name',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='salesprice',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='static_attr',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='type',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='typeattr',
            name='attr_type',
        ),
        migrations.AddField(
            model_name='goods',
            name='sav',
            field=django_pgjsonb.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, default=1, decode_kwargs={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='typeattr',
            name='type',
            field=models.CharField(default='s', max_length=2, choices=[('s', 'static'), ('d', 'dynamic'), ('Ys', 'system_static'), ('Yd', 'system_dynamic')]),
        ),
    ]
