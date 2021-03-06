# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='item_free',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='memo',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='memo',
            name='paid',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='free',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchasememo',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='purchasememo',
            name='paid',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='free',
            field=models.IntegerField(default=0),
        ),
    ]
