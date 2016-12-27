# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='nickname', max_length=60)),
                ('phone', models.CharField(null=True, unique=True, max_length=11, blank=True)),
                ('qq', models.CharField(null=True, unique=True, max_length=13, blank=True)),
                ('wx', models.CharField(null=True, unique=True, max_length=20, blank=True)),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='joined')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'WYSusers',
                'verbose_name': 'WYSuser',
            },
        ),
    ]
