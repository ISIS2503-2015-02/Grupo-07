# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default=b'a@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
