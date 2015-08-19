# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movibuses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaMobiBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Reserva', blank=True)),
                ('movi_bus', models.OneToOneField(null=True, to='movibuses.MoviBus')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(unique=True, max_length=200)),
                ('contrasenia', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime(1980, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservamobibus',
            name='usuario',
            field=models.OneToOneField(null=True, to='usuarios.Usuario'),
        ),
    ]
