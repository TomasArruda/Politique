# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoCapacitacao',
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
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(default=b'', max_length=100)),
                ('data', models.DateField()),
                ('feedback', models.CharField(default=b'', max_length=500)),
                ('tipoEvento', models.CharField(default=b'0', max_length=1)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CapacitacaoInterna',
            fields=[
                ('evento_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Website.Evento')),
                ('material', models.CharField(default=b'', max_length=200)),
            ],
            options={
            },
            bases=('Website.evento',),
        ),
        migrations.CreateModel(
            name='CapacitacaoExterna',
            fields=[
                ('evento_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Website.Evento')),
                ('custo', models.CharField(default=b'', max_length=100)),
                ('palestrante', models.CharField(default=b'', max_length=100)),
            ],
            options={
            },
            bases=('Website.evento',),
        ),
        migrations.CreateModel(
            name='EventoInstitucional',
            fields=[
                ('evento_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Website.Evento')),
                ('custo', models.CharField(default=b'', max_length=100)),
                ('motivoPatrocinio', models.CharField(default=b'', max_length=500)),
                ('empresasParceiras', models.ManyToManyField(to='Website.EmpresaParceira')),
            ],
            options={
            },
            bases=('Website.evento',),
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
                ('missao', models.CharField(default=b'', max_length=150)),
                ('anoFundacao', models.IntegerField(default=0)),
                ('website', models.CharField(default=b'', max_length=100)),
                ('parceiros', models.CharField(default=b'', max_length=500)),
                ('principaisProgramas', models.CharField(default=b'', max_length=500)),
                ('apoio', models.CharField(default=b'', max_length=100)),
                ('realizada', models.BooleanField()),
                ('percepcaoPresenca', models.CharField(default=b'', max_length=100)),
                ('contato', models.CharField(default=b'', max_length=100)),
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
                ('permissao', models.IntegerField(default=0)),
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
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('eventos', models.ManyToManyField(to='Website.Evento')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('setor', models.ForeignKey(to='Website.Setor', null=True)),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='telefone',
            name='membro',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='iniciativa',
            name='membro',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='financiamento',
            name='membro',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
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
            field=models.ForeignKey(default=b'', to='Website.TipoParceria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contatoiniciativa',
            name='iniciativa',
            field=models.ForeignKey(default=b'', to='Website.Iniciativa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contatocapacitacao',
            name='capacitacaoExterna',
            field=models.ForeignKey(default=b'', to='Website.CapacitacaoExterna'),
            preserve_default=True,
        ),
    ]
