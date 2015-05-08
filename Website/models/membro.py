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

class Membro(AbstractBaseUser):
	nome = models.CharField(max_length=100, blank=False, default='', null=False)
	email = models.EmailField(blank=False, null=False, default='')
	
	eventos = models.ManyToManyField('Evento')
	setor = models.ForeignKey('Setor',default='')

	USERNAME_FIELD = 'nome'
	REQUIRED_FIELDS = ['email', 'password']

	def save(self, *args, **kwargs):
		self.password = make_password(self.password)
		super(Admin, self).save(*args, **kwargs)

	class  Meta:
		ordering = ('nome',)