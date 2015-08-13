# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150811_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstacionVcub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=200)),
                ('fecha_construccion', models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Construccion', blank=True)),
                ('cap_actual', models.IntegerField()),
                ('cap_max', models.IntegerField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('estado_operativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vcub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registro', models.CharField(unique=True, max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('fecha_fabricacion', models.DateField(default=datetime.datetime(2010, 1, 1, 17, 56, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Fabricacion', blank=True)),
                ('en_transito', models.BooleanField(default=True)),
                ('estado_operativo', models.BooleanField(default=True)),
                ('estacion', models.ForeignKey(to='main.EstacionVcub', null=True)),
            ],
        ),
    ]
