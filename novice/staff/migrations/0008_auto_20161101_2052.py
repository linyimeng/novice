# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_empinfo_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empinfo',
            name='job',
            field=models.ForeignKey(to='staff.Jobs', blank=True, null=True),
        ),
    ]
