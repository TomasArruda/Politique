# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapacitacaoExterna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('custo', models.CharField(default=b'', max_length=100)),
                ('palestrante', models.CharField(default=b'', max_length=100)),
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
                ('material', models.CharField(default=b'', max_length=200)),
                ('evento', models.ForeignKey(default=b'', to='Website.Evento')),
            ],
            options={
                'ordering': ('evento',),
            },
            bases=(models.Model,),
        ),
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
            name='EventoInstitucional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('custo', models.CharField(default=b'', max_length=100)),
                ('mostivoPatrocinio', models.CharField(default=b'', max_length=500)),
                ('empresasParceiras', models.ManyToManyField(to='Website.EmpresaParceira')),
                ('evento', models.ForeignKey(default=b'', to='Website.Evento')),
            ],
            options={
                'ordering': ('evento',),
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
                ('vencedoresAnteriores', models.CharField(default=b'', max_length=500)),
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
                ('questoesChaves', models.CharField(default=b'', max_length=500)),
                ('areaAtuacao', models.CharField(default=b'', max_length=100)),
                ('anoFundacao', models.IntegerField(default=0)),
                ('website', models.CharField(default=b'', max_length=100)),
                ('parceiros', models.CharField(default=b'', max_length=500)),
                ('principaisProgramas', models.CharField(default=b'', max_length=500)),
                ('apoio', models.CharField(default=b'', max_length=100)),
                ('percepcaoPresenca', models.CharField(default=b'', max_length=100)),
                ('Realizada', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(default=b'', max_length=75)),
                ('eventos', models.ManyToManyField(to='Website.Evento')),
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
                ('Permissao', models.CharField(default=b'', max_length=150)),
            ],
            options={
                'ordering': ('nome',),
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
            model_name='membro',
            name='setor',
            field=models.ForeignKey(default=b'', to='Website.Setor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membro',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iniciativa',
            name='membro',
            field=models.ForeignKey(default=b'', to='Website.Membro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='financiamento',
            name='membro',
            field=models.ForeignKey(default=b'', to='Website.Membro'),
            preserve_default=True,
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
    ]
