# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjsonb.fields
from django.conf import settings
import django.core.serializers.json


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('gsav', django_pgjsonb.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={})),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='deleted', blank=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
                ('lastmodifyer', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='lastmodifyer', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='deleted', blank=True)),
                ('superiors', models.ForeignKey(to='goods.Type', default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=30)),
                ('keyname', models.CharField(unique=True, max_length=30)),
                ('type', models.CharField(choices=[('s', 'static'), ('d', 'dynamic'), ('ss', 'system_static'), ('sd', 'system_dynamic')], default='s', max_length=2)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='deleted', blank=True)),
                ('goodstype', models.ForeignKey(to='goods.Type')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(to='goods.Type'),
        ),
    ]
