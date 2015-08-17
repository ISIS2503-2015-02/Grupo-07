# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150816_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alertatranvia',
            old_name='solicits_reposicion',
            new_name='solicita_reposicion',
        ),
    ]
