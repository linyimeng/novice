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
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=80)),
                ('customid', models.CharField(null=True, blank=True, unique=True, max_length=30)),
                ('is_vendor', models.BooleanField(verbose_name='is vendor', default=False)),
                ('is_client', models.BooleanField(verbose_name='is client', default=False)),
                ('landline', models.CharField(null=True, verbose_name='landline', blank=True, max_length=20)),
                ('phone', models.CharField(null=True, verbose_name='phone', blank=True, unique=True, max_length=12)),
                ('email', models.EmailField(null=True, blank=True, unique=True, max_length=254)),
                ('fax', models.CharField(null=True, verbose_name='fax', blank=True, max_length=30)),
                ('joined', models.DateTimeField(verbose_name='joined', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='deleted', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(null=True, blank=True, max_length=255)),
                ('landline', models.CharField(null=True, verbose_name='landline', blank=True, max_length=20)),
                ('phone', models.CharField(null=True, verbose_name='phone', blank=True, unique=True, max_length=12)),
                ('email', models.EmailField(null=True, blank=True, unique=True, max_length=254)),
                ('fax', models.CharField(null=True, verbose_name='fax', blank=True, max_length=30)),
                ('joined', models.DateTimeField(verbose_name='joined', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='deleted', blank=True)),
                ('company', models.ForeignKey(blank=True, null=True, to='bp.Company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
