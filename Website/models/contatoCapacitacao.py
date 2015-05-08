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

class ContatoCapacitacao(models.Model):
	contatos = models.CharField(max_length=500, blank=False, default='', null=False)

	capacitacaoExterna = models.ForeignKey('CapacitacaoExterna',default='', null=False, blank = False)
	
	class  Meta:
		ordering = ('id',)