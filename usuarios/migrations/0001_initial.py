# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaMobiBus',
            fields=[
                ('identificador', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_programada', models.DateTimeField(default=datetime.datetime(2015, 11, 24, 10, 29, 8, 674179))),
                ('usuario', models.ForeignKey(related_name='reserva', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
