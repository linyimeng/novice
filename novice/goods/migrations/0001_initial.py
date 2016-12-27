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
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('customid', models.CharField(null=True, blank=True, unique=True, max_length=30)),
                ('name', models.CharField(max_length=120)),
                ('manufacturer', models.CharField(max_length=226)),
                ('barcode', models.CharField(null=True, blank=True, max_length=30)),
                ('salesprice', models.DecimalField(max_digits=12, decimal_places=4)),
                ('costprice', models.DecimalField(max_digits=12, decimal_places=4)),
                ('is_active', models.BooleanField(default=True)),
                ('main_attr', models.TextField()),
                ('custom_attr', models.TextField()),
                ('other_attr', models.TextField()),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='deleted', blank=True)),
                ('lastmodifyer', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='lastmodifyer', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True, verbose_name='deleted', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAttr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('attr_type', models.CharField(choices=[('main', 'main_attr'), ('other', 'other_attr'), ('custom', 'custom_attr')], default='main', max_length=6)),
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
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
