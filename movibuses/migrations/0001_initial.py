# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConductorMoviBus',
            fields=[
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('calificacion', models.IntegerField(default=0)),
                ('fecha_ingreso_sistema', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_nacimiento', models.DateField(default=datetime.datetime(1980, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoordenadasMoviBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('latitud', models.FloatField(default=1)),
                ('longitud', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MoviBus',
            fields=[
                ('placa', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('fecha_fabricacion', models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion', blank=True)),
                ('cap_max', models.IntegerField()),
                ('ruta', models.CharField(max_length=1, blank=True)),
                ('estado_operativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecorridoMoviBus',
            fields=[
                ('identificador', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('fin', models.DateTimeField(auto_now_add=True)),
                ('conductor', models.ForeignKey(related_name='recorrido', to='movibuses.ConductorMoviBus')),
                ('movibus', models.ForeignKey(related_name='recorrido', to='movibuses.MoviBus')),
                ('reserva', models.ForeignKey(related_name='recorrido', to='usuarios.ReservaMobiBus')),
            ],
        ),
        migrations.CreateModel(
            name='ReporteMoviBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('movibus', models.ForeignKey(related_name='reporte', to='movibuses.MoviBus')),
            ],
        ),
        migrations.AddField(
            model_name='coordenadasmovibus',
            name='movibus',
            field=models.ForeignKey(related_name='coordenada', to='movibuses.MoviBus'),
        ),
        migrations.AddField(
            model_name='coordenadasmovibus',
            name='recorrido',
            field=models.ForeignKey(related_name='coordena', default=None, blank=True, to='movibuses.RecorridoMoviBus', null=True),
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
