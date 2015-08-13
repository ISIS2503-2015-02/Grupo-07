# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('fecha_de_nacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConductorTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.CharField(unique=True, max_length=200)),
                ('fecha_de_nacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoviBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(unique=True, max_length=200)),
                ('fecha_fabricacion', models.DateField(verbose_name=b'Fecha de Fabricacion', blank=True)),
                ('cap_max', models.IntegerField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('estado_operativo', models.BooleanField(default=True)),
                ('conductor', models.OneToOneField(null=True, to='main.ConductorMoviBus')),
            ],
        ),
        migrations.CreateModel(
            name='Tranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(unique=True, max_length=200)),
                ('fecha_fabricacion', models.DateField(verbose_name=b'Fecha de Fabricacion', blank=True)),
                ('cap_max', models.IntegerField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('estado_operativo', models.BooleanField(default=True)),
                ('conductor', models.OneToOneField(null=True, to='main.ConductorTranvia')),
            ],
        ),
    ]
