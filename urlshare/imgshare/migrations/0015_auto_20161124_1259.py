# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0014_auto_20161124_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='key',
            field=models.SlugField(max_length=10, unique=True),
        ),
    ]
