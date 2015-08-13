# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150811_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movibus',
            name='modelo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tranvia',
            name='modelo',
            field=models.CharField(max_length=200),
        ),
    ]
