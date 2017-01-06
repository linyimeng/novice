# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.serializers.json
import django_pgjsonb.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('quantity', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price', models.DecimalField(max_digits=18, decimal_places=8)),
                ('gdav', django_pgjsonb.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={})),
                ('gsav', django_pgjsonb.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={})),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='joined')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
                ('goods', models.ForeignKey(to='goods.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ordercode', models.CharField(primary_key=True, serialize=False, max_length=30)),
                ('status', models.CharField(default='N', max_length=10)),
                ('totalquantity', models.DecimalField(max_digits=10, decimal_places=2)),
                ('totalprice', models.DecimalField(max_digits=18, decimal_places=8)),
                ('remark', models.TextField(blank=True, null=True)),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='joined')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
                ('company', models.ForeignKey(to='partner.Company', null=True, blank=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('personal', models.ForeignKey(related_name='personal', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('io', models.CharField(choices=[('I', 'in'), ('O', 'out')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.ForeignKey(to='order.Type'),
        ),
        migrations.AddField(
            model_name='detail',
            name='order',
            field=models.ForeignKey(to='order.Order'),
        ),
    ]
