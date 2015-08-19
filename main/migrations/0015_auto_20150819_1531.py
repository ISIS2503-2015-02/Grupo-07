# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_coordenadastranvia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertatranvia',
            name='tranvia',
        ),
        migrations.RemoveField(
            model_name='coordenadasmovibus',
            name='movibus',
        ),
        migrations.RemoveField(
            model_name='coordenadastranvia',
            name='tranvia',
        ),
        migrations.RemoveField(
            model_name='movibus',
            name='conductor',
        ),
        migrations.RemoveField(
            model_name='reservamobibus',
            name='movi_bus',
        ),
        migrations.RemoveField(
            model_name='reservamobibus',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='tranvia',
            name='conductor',
        ),
        migrations.RemoveField(
            model_name='tranvia',
            name='linea',
        ),
        migrations.RemoveField(
            model_name='vcub',
            name='estacion',
        ),
        migrations.DeleteModel(
            name='AlertaTranvia',
        ),
        migrations.DeleteModel(
            name='ConductorMoviBus',
        ),
        migrations.DeleteModel(
            name='ConductorTranvia',
        ),
        migrations.DeleteModel(
            name='CoordenadasMoviBus',
        ),
        migrations.DeleteModel(
            name='CoordenadasTranvia',
        ),
        migrations.DeleteModel(
            name='EstacionVcub',
        ),
        migrations.DeleteModel(
            name='Linea',
        ),
        migrations.DeleteModel(
            name='MoviBus',
        ),
        migrations.DeleteModel(
            name='ReservaMobiBus',
        ),
        migrations.DeleteModel(
            name='Tranvia',
        ),
        migrations.DeleteModel(
            name='Vcub',
        ),
    ]
