# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150819_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordenadasTranvia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime(2010, 1, 1, 18, 0, 0, 775217, tzinfo=utc), verbose_name=b'Fecha', blank=True)),
                ('latitud', models.FloatField(default=1)),
                ('longitud', models.FloatField(default=1)),
                ('tranvia', models.ForeignKey(to='main.Tranvia', null=True)),
            ],
        ),
    ]
