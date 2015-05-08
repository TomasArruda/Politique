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

class EmpresaParceira(models.Model):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	ramoAtuacao = models.CharField(max_length=100, blank=False, default='', null=False)
	background = models.CharField(max_length=100, blank=False, default='', null=False)
	apoios = models.CharField(max_length=100, blank=False, default='', null=False)
	propostaApoio = models.CharField(max_length=100, blank=False, default='', null=False)

	tipoParceria = models.ForeignKey('TipoParceria',default='', null=False, blank = False)
	iniciativas = models.ManyToManyField('Iniciativa')

	class  Meta:
		ordering = ('nome',)