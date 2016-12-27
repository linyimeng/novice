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
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=60, verbose_name='department name')),
                ('customid', models.CharField(blank=True, unique=True, null=True, max_length=30)),
                ('joined', models.DateTimeField(verbose_name='joined', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='deleted')),
            ],
            options={
                'verbose_name': 'department',
            },
        ),
        migrations.CreateModel(
            name='EmpInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=60, verbose_name='full name')),
                ('customid', models.CharField(blank=True, unique=True, null=True, max_length=30)),
                ('work_address', models.CharField(blank=True, max_length=255, verbose_name='work address', null=True)),
                ('office_phone', models.CharField(blank=True, unique=True, verbose_name='office phone', null=True, max_length=12)),
                ('office_address', models.CharField(blank=True, max_length=255, verbose_name='office address', null=True)),
                ('office_email', models.EmailField(blank=True, unique=True, null=True, max_length=254)),
                ('office_landline', models.CharField(blank=True, max_length=20, verbose_name='landline', null=True)),
                ('cardid', models.CharField(blank=20, max_length=20, verbose_name='cardid', null=True)),
                ('bank_account', models.CharField(blank=True, max_length=36, verbose_name='bank Account', null=True)),
                ('sex', models.CharField(blank=True, max_length=2, verbose_name='sex', null=True)),
                ('marital_status', models.CharField(blank=True, max_length=6, verbose_name='marital status', null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('isarchive', models.BooleanField(verbose_name='is archive', default=False)),
                ('entry_time', models.DateTimeField(blank=True)),
                ('joined', models.DateTimeField(verbose_name='joined', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='deleted')),
                ('department', models.ForeignKey(to='staff.Department')),
            ],
            options={
                'verbose_name': 'staffinfo',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='jobname')),
                ('joined', models.DateTimeField(verbose_name='joined', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='deleted')),
                ('department', models.ForeignKey(to='staff.Department')),
            ],
            options={
                'verbose_name': 'position',
            },
        ),
        migrations.AddField(
            model_name='empinfo',
            name='job',
            field=models.ForeignKey(to='staff.Jobs'),
        ),
        migrations.AddField(
            model_name='empinfo',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(related_name='empinfo', blank=True, null=True, to='staff.EmpInfo'),
        ),
        migrations.AddField(
            model_name='department',
            name='superiors',
            field=models.ForeignKey(to='staff.Department', blank=True, null=True, default=None),
        ),
    ]
