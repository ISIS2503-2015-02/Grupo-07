# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tranvias', '0003_auto_20150819_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='linea',
            name='kilometros_totales',
            field=models.FloatField(default=0),
        ),
    ]
