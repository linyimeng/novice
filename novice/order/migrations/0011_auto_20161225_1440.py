# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20161225_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='personal',
            field=models.ForeignKey(blank=True, related_name='personal', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
