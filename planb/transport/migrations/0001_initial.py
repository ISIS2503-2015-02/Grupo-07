# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude_pos', models.CharField(max_length=20)),
                ('longitude_pos', models.CharField(max_length=20)),
                ('transport_speed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driver_name', models.CharField(max_length=30)),
                ('license_plate', models.CharField(max_length=10)),
                ('transport_type', models.IntegerField()),
                ('transport_status', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='historic',
            name='transport_pk',
            field=models.ForeignKey(to='transport.Transport'),
        ),
    ]
