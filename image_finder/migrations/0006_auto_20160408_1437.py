# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-08 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_finder', '0005_imagedetail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetail',
            name='image',
            field=models.FileField(upload_to='ImageLocalFinder/static/attachments'),
        ),
    ]
