# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'course', 'verbose_name_plural': 'courses'},
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='courses.Student'),
        ),
    ]
