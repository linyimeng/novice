# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_department_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='empinfo',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]
