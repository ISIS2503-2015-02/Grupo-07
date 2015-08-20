# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tranvias', '0002_auto_20150819_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductortranvia',
            name='calificacion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='conductortranvia',
            name='fecha_ingreso_sistema',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de ingreso al sistema', blank=True),
        ),
        migrations.AddField(
            model_name='conductortranvia',
            name='kilometros_recorridos',
            field=models.FloatField(default=0),
        ),
    ]
