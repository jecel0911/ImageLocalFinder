# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-08 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import functools
import image_finder.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_finder', '0006_auto_20160408_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetail',
            name='image',
            field=models.FileField(upload_to=functools.partial(image_finder.models._update_filename, *(), **{'path': 'ImageLocalFinder/static/attachments'})),
        ),
    ]
