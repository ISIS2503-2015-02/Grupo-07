# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tranvias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertatranvia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Alerta', blank=True),
        ),
        migrations.AlterField(
            model_name='conductortranvia',
            name='fecha_de_nacimiento',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='conductortranvia',
            name='fecha_ingreso_sistema',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de ingreso al sistema', blank=True),
        ),
        migrations.AlterField(
            model_name='coordenadastranvia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True),
        ),
        migrations.AlterField(
            model_name='reportetranvia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True),
        ),
        migrations.AlterField(
            model_name='tranvia',
            name='fecha_fabricacion',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion', blank=True),
        ),
    ]
