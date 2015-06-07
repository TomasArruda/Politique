# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iniciativa',
            name='membro',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
