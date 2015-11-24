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
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(default=b'Alerta Tranvia', max_length=200, null=True)),
                ('solicita_reposicion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ConductorTranvia',
            fields=[
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('calificacion', models.IntegerField(default=0)),
                ('fecha_ingreso_sistema', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_nacimiento', models.DateField(default=datetime.datetime(1980, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoordenadasTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('latitud', models.FloatField(default=1)),
                ('longitud', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('numero', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('estacion_llegada', models.CharField(max_length=200, null=True)),
                ('estacion_salida', models.CharField(max_length=200, null=True)),
                ('kilometros_totales', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RecorridoTranvia',
            fields=[
                ('identificador', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('inicio', models.DateTimeField(auto_now_add=True)),
                ('fin', models.DateTimeField(auto_now_add=True)),
                ('conductor', models.ForeignKey(related_name='recorrido', to='tranvias.ConductorTranvia')),
                ('linea', models.ForeignKey(related_name='recorrido', to='tranvias.Linea')),
            ],
        ),
        migrations.CreateModel(
            name='ReporteTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tranvia',
            fields=[
                ('placa', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('fecha_fabricacion', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion')),
                ('cap_max', models.IntegerField()),
                ('estado_operativo', models.BooleanField(default=True)),
                ('linea', models.ForeignKey(related_name='tranvia', to='tranvias.Linea')),
            ],
        ),
        migrations.AddField(
            model_name='reportetranvia',
            name='tranvia',
            field=models.ForeignKey(related_name='reporte', to='tranvias.Tranvia'),
        ),
        migrations.AddField(
            model_name='recorridotranvia',
            name='tranvia',
            field=models.ForeignKey(related_name='recorrido', to='tranvias.Tranvia'),
        ),
        migrations.AddField(
            model_name='coordenadastranvia',
            name='recorrido',
            field=models.ForeignKey(related_name='coordenada', default=None, blank=True, to='tranvias.RecorridoTranvia', null=True),
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
