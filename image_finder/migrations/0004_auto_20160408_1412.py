# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-08 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_finder', '0003_auto_20160407_1216'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileUploaded',
        ),
        migrations.RemoveField(
            model_name='imagedetail',
            name='image',
        ),
    ]
