# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20161113_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='user',
            new_name='creator',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='customid',
        ),
    ]
