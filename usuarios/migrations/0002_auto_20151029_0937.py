# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservamobibus',
            name='fecha_programada',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 29, 9, 37, 16, 385243)),
        ),
    ]
