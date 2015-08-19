# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0011_auto_20150819_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservamobibus',
            name='usuario',
            field=models.OneToOneField(null=True, to='users.Usuario'),
        ),
    ]
