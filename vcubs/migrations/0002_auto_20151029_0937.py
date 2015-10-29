# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vcubs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionvcub',
            name='fecha_construccion',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Construccion', blank=True),
        ),
        migrations.AlterField(
            model_name='vcub',
            name='fecha_fabricacion',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion', blank=True),
        ),
    ]
