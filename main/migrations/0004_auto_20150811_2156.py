# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150811_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='movibus',
            name='linea',
            field=models.CharField(max_length=1, blank=True),
        ),
        migrations.AddField(
            model_name='tranvia',
            name='linea',
            field=models.CharField(max_length=1, blank=True),
        ),
    ]
