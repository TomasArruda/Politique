# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0005_auto_20150508_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacaoexterna',
            name='custo',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacaoexterna',
            name='palestrante',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacaointerna',
            name='material',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventoinstitucional',
            name='custo',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='financiamento',
            name='vencedoresAnteriores',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='parceiros',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='principaisProgramas',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='iniciativa',
            name='questoesChaves',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setor',
            name='Permissao',
            field=models.CharField(default=b'', max_length=150),
            preserve_default=True,
        ),
    ]
