# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20161029_1029'),
        ('staff', '0008_auto_20161101_2052'),
        ('bp', '0003_auto_20161029_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('dynamic_attr', models.TextField(null=True, blank=True)),
                ('remark', models.TextField(null=True, blank=True)),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='joined')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
                ('goods', models.ForeignKey(to='goods.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ordercode', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('totalquantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalprice', models.DecimalField(decimal_places=10, max_digits=10)),
                ('remark', models.TextField(null=True, blank=True)),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='joined')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('deleted', models.DateTimeField(null=True, blank=True, verbose_name='deleted')),
                ('company', models.ForeignKey(to='bp.Company')),
                ('creator', models.ForeignKey(to='staff.EmpInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('io', models.CharField(max_length=1, choices=[('I', 'in'), ('O', 'out')])),
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
