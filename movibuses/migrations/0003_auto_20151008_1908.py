# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movibuses', '0002_auto_20150917_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductormovibus',
            name='fecha_de_nacimiento',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='conductormovibus',
            name='fecha_ingreso_sistema',
            field=models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de ingreso al sistema', blank=True),
        ),
        migrations.AlterField(
            model_name='coordenadasmovibus',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True),
        ),
        migrations.AlterField(
            model_name='movibus',
            name='fecha_fabricacion',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion', blank=True),
        ),
        migrations.AlterField(
            model_name='reportemovibus',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True),
        ),
    ]
