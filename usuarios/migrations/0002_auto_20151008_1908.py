# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservamobibus',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Reserva', blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True),
        ),
    ]
