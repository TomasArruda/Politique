# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('data', models.DateField()),
                ('feedback', models.CharField(default=b'', max_length=500)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
    ]
