# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapacitacaoExterna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('custo', models.CharField(default=b'', max_length=500)),
                ('palestrante', models.CharField(default=b'', max_length=500)),
                ('evento', models.ForeignKey(default=b'', to='Website.Evento')),
            ],
            options={
                'ordering': ('evento',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CapacitacaoInterna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('material', models.CharField(default=b'', max_length=500)),
                ('evento', models.ForeignKey(default=b'', to='Website.Evento')),
            ],
            options={
                'ordering': ('evento',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventoInstitucional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('custo', models.CharField(default=b'', max_length=500)),
                ('mostivoPatrocinio', models.CharField(default=b'', max_length=500)),
                ('evento', models.ForeignKey(default=b'', to='Website.Evento')),
            ],
            options={
                'ordering': ('evento',),
            },
            bases=(models.Model,),
        ),
    ]
