# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 13:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images')),
                ('desc', models.CharField(blank=True, max_length=120)),
                ('key', models.SlugField(max_length=10, unique=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime.now)),
                ('view_date', models.DateTimeField(default=datetime.datetime.now)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('like_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
