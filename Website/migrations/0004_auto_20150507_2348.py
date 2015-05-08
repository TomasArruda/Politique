# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_auto_20150507_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoCapacitacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contatos', models.CharField(default=b'', max_length=500)),
                ('capacitacaoExterna', models.ForeignKey(default=b'', to='Website.CapacitacaoExterna')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(unique=True, max_length=128)),
                ('membro', models.ForeignKey(default=b'', to='Website.Membro')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='membro',
            name='feedback',
        ),
        migrations.AddField(
            model_name='membro',
            name='eventos',
            field=models.ManyToManyField(to='Website.Evento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(default=b'', max_length=75),
            preserve_default=True,
        ),
    ]
