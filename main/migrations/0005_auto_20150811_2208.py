# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150811_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movibus',
            old_name='linea',
            new_name='ruta',
        ),
    ]
