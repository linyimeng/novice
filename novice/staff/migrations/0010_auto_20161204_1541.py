# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_department_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='img',
        ),
        migrations.AddField(
            model_name='department',
            name='imgurl',
            field=models.CharField(blank=True, null=True, max_length=120),
        ),
    ]
