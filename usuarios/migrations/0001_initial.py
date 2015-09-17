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
            name='ReservaMobiBus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Reserva', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('login', models.CharField(unique=True, max_length=200)),
                ('contrasenia', models.CharField(max_length=200)),
                ('direccion', models.CharField(default=b'', max_length=200)),
                ('telefono', models.CharField(default=b'', max_length=200)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime(1980, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha de Nacimiento', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservamobibus',
            name='usuario',
            field=models.ForeignKey(related_name='reserva', to='usuarios.Usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='reservamobibus',
            unique_together=set([('usuario', 'fecha')]),
        ),
    ]
