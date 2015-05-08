# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_auto_20150507_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoIniciativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contatos', models.CharField(default=b'', max_length=500)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmpresaParceira',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('ramoAtuacao', models.CharField(default=b'', max_length=100)),
                ('background', models.CharField(default=b'', max_length=100)),
                ('apoios', models.CharField(default=b'', max_length=100)),
                ('propostaApoio', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Financiamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('processo', models.CharField(default=b'', max_length=100)),
                ('tema', models.CharField(default=b'', max_length=100)),
                ('projetos', models.CharField(default=b'', max_length=100)),
                ('valor', models.CharField(default=b'', max_length=100)),
                ('prazos', models.CharField(default=b'', max_length=100)),
                ('instituicaoResponsavel', models.CharField(default=b'', max_length=100)),
                ('vencedoresAnteriores', models.CharField(default=b'', max_length=100)),
                ('membro', models.ForeignKey(default=b'', to='Website.Membro')),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Iniciativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('data', models.DateField()),
                ('tipoMembro', models.CharField(default=b'', max_length=100)),
                ('publicoAlvo', models.CharField(default=b'', max_length=100)),
                ('duracao', models.CharField(default=b'', max_length=100)),
                ('questoesChaves', models.CharField(default=b'', max_length=100)),
                ('areaAtuacao', models.CharField(default=b'', max_length=100)),
                ('anoFundacao', models.IntegerField(default=0)),
                ('website', models.CharField(default=b'', max_length=100)),
                ('parceiros', models.CharField(default=b'', max_length=100)),
                ('principaisProgramas', models.CharField(default=b'', max_length=100)),
                ('apoio', models.CharField(default=b'', max_length=100)),
                ('percepcaoPresenca', models.CharField(default=b'', max_length=100)),
                ('Realizada', models.BooleanField(default=True)),
                ('membro', models.ForeignKey(default=b'', to='Website.Membro')),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoParceria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='empresaparceira',
            name='iniciativas',
            field=models.ManyToManyField(to='Website.Iniciativa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empresaparceira',
            name='tipoParceria',
            field=models.ForeignKey(default=b'', to='Website.TipoParceria'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contatoiniciativa',
            name='iniciativa',
            field=models.ForeignKey(default=b'', to='Website.Iniciativa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventoinstitucional',
            name='empresasParceiras',
            field=models.ManyToManyField(to='Website.EmpresaParceira'),
            preserve_default=True,
        ),
    ]
