# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_capacitacaoexterna_capacitacaointerna_eventoinstitucional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=75, blank=True)),
                ('feedback', models.CharField(default=b'', max_length=500)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('Permissao', models.CharField(default=b'', max_length=500)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membro',
            name='setor',
            field=models.ForeignKey(default=b'', to='Website.Setor'),
            preserve_default=True,
        ),
    ]
