# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150817_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(unique=True)),
                ('estacion_llegada', models.CharField(max_length=200, null=True)),
                ('estacion_salida', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movibus',
            name='kilometraje',
            field=models.FloatField(default=1, blank=True),
        ),
        migrations.AddField(
            model_name='tranvia',
            name='kilometraje',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='alertatranvia',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Alerta', blank=True),
        ),
        migrations.AlterField(
            model_name='alertatranvia',
            name='tranvia',
            field=models.ForeignKey(to='main.Tranvia', null=True),
        ),
        migrations.AlterField(
            model_name='tranvia',
            name='linea',
            field=models.ForeignKey(blank=True, to='main.Linea', null=True),
        ),
        migrations.AlterField(
            model_name='vcub',
            name='estacion',
            field=models.ForeignKey(blank=True, to='main.EstacionVcub', null=True),
        ),
    ]
