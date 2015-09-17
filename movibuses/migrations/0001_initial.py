# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConductorMoviBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.CharField(unique=True, max_length=200)),
                ('calificacion', models.IntegerField(default=0)),
                ('kilometros_recorridos', models.FloatField(default=0)),
                ('fecha_ingreso_sistema', models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de ingreso al sistema', blank=True)),
                ('fecha_de_nacimiento', models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoordenadasMoviBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True)),
                ('latitud', models.FloatField(default=1)),
                ('longitud', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MoviBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('kilometraje', models.FloatField(default=1, blank=True)),
                ('fecha_fabricacion', models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion', blank=True)),
                ('cap_max', models.IntegerField()),
                ('ruta', models.CharField(max_length=1, blank=True)),
                ('estado_operativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReporteMoviBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True)),
                ('movibus', models.ForeignKey(related_name='reporte', to='movibuses.MoviBus')),
            ],
        ),
        migrations.AddField(
            model_name='coordenadasmovibus',
            name='movibus',
            field=models.ForeignKey(related_name='coordenada', to='movibuses.MoviBus'),
        ),
        migrations.AddField(
            model_name='conductormovibus',
            name='movibus',
            field=models.ForeignKey(related_name='conductor', to='movibuses.MoviBus'),
        ),
        migrations.AlterUniqueTogether(
            name='reportemovibus',
            unique_together=set([('movibus', 'fecha')]),
        ),
        migrations.AlterUniqueTogether(
            name='coordenadasmovibus',
            unique_together=set([('movibus', 'fecha')]),
        ),
    ]
