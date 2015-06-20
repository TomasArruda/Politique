# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
    ]
