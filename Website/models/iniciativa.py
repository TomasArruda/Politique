from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from datetime import date
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.dispatch import receiver
from django.db.models.signals import post_save
import binascii
import os

class Iniciativa(models.Model):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	data = models.DateField(auto_now=False, null=False, blank=False)

	tipoMembro = models.CharField(max_length=100, blank=False, default='', null=False)
	publicoAlvo = models.CharField(max_length=100, blank=False, default='', null=False)
	duracao = models.CharField(max_length=100, blank=False, default='', null=False)
	questoesChaves = models.CharField(max_length=500, blank=False, default='', null=False)
	areaAtuacao = models.CharField(max_length=100, blank=False, default='', null=False)
	anoFundacao = models.IntegerField(default=0)
	website = models.CharField(max_length=100, blank=False, default='', null=False)
	parceiros = models.CharField(max_length=500, blank=False, default='', null=False)
	principaisProgramas = models.CharField(max_length=500, blank=False, default='', null=False)
	apoio = models.CharField(max_length=100, blank=False, default='', null=False)
	percepcaoPresenca = models.CharField(max_length=100, blank=False, default='', null=False)
	Realizada = models.BooleanField(default=True)

	membro = models.ForeignKey('Membro',default='', null=False, blank = False)

	class  Meta:
		ordering = ('nome',)