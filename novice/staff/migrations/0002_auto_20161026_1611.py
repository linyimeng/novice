# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name': 'jobs'},
        ),
        migrations.RemoveField(
            model_name='empinfo',
            name='office_email',
        ),
        migrations.AddField(
            model_name='empinfo',
            name='email',
            field=models.EmailField(default=datetime.datetime(2016, 10, 26, 8, 11, 13, 845442, tzinfo=utc), unique=True, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='customid',
            field=models.CharField(null=True, default=None, unique=True, blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='entry_time',
            field=models.DateTimeField(),
        ),
    ]
