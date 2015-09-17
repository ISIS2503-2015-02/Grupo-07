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
            name='AlertaTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Alerta', blank=True)),
                ('solicita_reposicion', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConductorTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.CharField(unique=True, max_length=200)),
                ('calificacion', models.IntegerField(default=0)),
                ('kilometros_recorridos', models.FloatField(default=0)),
                ('fecha_ingreso_sistema', models.DateField(default=datetime.datetime(1980, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de ingreso al sistema', blank=True)),
                ('fecha_de_nacimiento', models.DateField(default=datetime.datetime(1980, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoordenadasTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True)),
                ('latitud', models.FloatField(default=1)),
                ('longitud', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(unique=True, max_length=200)),
                ('estacion_llegada', models.CharField(max_length=200, null=True)),
                ('estacion_salida', models.CharField(max_length=200, null=True)),
                ('kilometros_totales', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReporteTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('kilometraje', models.FloatField(default=1)),
                ('fecha_fabricacion', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion', blank=True)),
                ('cap_max', models.IntegerField()),
                ('estado_operativo', models.BooleanField(default=True)),
                ('linea', models.ForeignKey(blank=True, to='tranvias.Linea', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='reportetranvia',
            name='tranvia',
            field=models.ForeignKey(related_name='reporte', to='tranvias.Tranvia'),
        ),
        migrations.AddField(
            model_name='coordenadastranvia',
            name='tranvia',
            field=models.ForeignKey(related_name='coordenada', to='tranvias.Tranvia'),
        ),
        migrations.AddField(
            model_name='conductortranvia',
            name='tranvia',
            field=models.ForeignKey(related_name='conductor', to='tranvias.Tranvia'),
        ),
        migrations.AddField(
            model_name='alertatranvia',
            name='tranvia',
            field=models.ForeignKey(related_name='alerta', to='tranvias.Tranvia'),
        ),
        migrations.AlterUniqueTogether(
            name='reportetranvia',
            unique_together=set([('tranvia', 'fecha')]),
        ),
        migrations.AlterUniqueTogether(
            name='coordenadastranvia',
            unique_together=set([('tranvia', 'fecha')]),
        ),
        migrations.AlterUniqueTogether(
            name='alertatranvia',
            unique_together=set([('tranvia', 'fecha')]),
        ),
    ]
