# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_type_superiors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='custom_attr',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='main_attr',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='other_attr',
        ),
        migrations.AddField(
            model_name='goods',
            name='static_attr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='typeattr',
            name='attr_type',
            field=models.CharField(max_length=10, default='static', choices=[('static', 'static'), ('dynamic', 'dynamic')]),
        ),
    ]
